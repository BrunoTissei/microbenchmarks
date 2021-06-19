#!/usr/bin/env python3

import os
import re
import sys
import argparse
import pandas as pd

from collections import defaultdict


class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

PATTERN = r"""
==========================================================================
Active Cores: [0-9]* of [0-9]*
Opcodes Processed: [0-9]* of [0-9]*
Total Progress\s*(\d*\.\d*)%
Global IPC\((\d*\.\d*)\)
Global ETC\((\d*\:\d*\:\d*)\)
==========================================================================
"""

END_PATTERN = r"""
End of dynamic simulation trace
End of Simulation
Writing FILE
Global_Statistics
#===============================================#
Global_Cycle: [0-9]*
Global_IPC: (\d*\.\d*)
Elapsed Time \([0-9]*:[0-9]*:[0-9]*\)
KIPS: [0-9]*\.[0-9]*
"""


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir',
                        type = str,
                        action = 'store',
                        required = True,
                        help = 'Directory with log files')

    parser.add_argument('--stat',
                        type = str,
                        action = 'store',
                        default = '',
                        required = False,
                        help = 'CSV file containing real IPC values')

    parser.add_argument('--compare',
                        type = str,
                        action = 'append',
                        default = [],
                        required = False,
                        help = 'Other directory with log files for comparing results')

    return parser.parse_args()

# Parses file and builds result dict with matched values
def get_result(file, result = {}):
    with open(file) as f:
        log_text = f.read()

    # Check if OrCS log is finished, then get results from finished log
    match = re.findall(END_PATTERN, log_text)
    if len(match) > 0:
        ipc = float(match[-1])

        result = {**result, **{
            'IPC':      f'{ipc:.3f}',
            'Progress': f'{"DONE"}'
        }}

        return result

    # If it's not finished, then get last result from unfinished log
    match = re.findall(PATTERN, log_text)
    if len(match) > 0:
        info = match[-1]

        progress = float(info[0])
        ipc      = float(info[1])
        etc      = info[2]

        result = {**result, **{
            'IPC':      f'{ipc:.3f}',
            'Progress': f'{progress:.2f}%',
            'ETC':      f'{etc}'
        }}

        return result

    # Otherwise, assume process hasn't stated yet.  It's also possible that
    # the log contains an error, and the process exited
    result['Progress'] = f'Not started'
    return result

# Builds results and outputs them
def main():
    args = parse_args()

    stats = {}
    compare = defaultdict(lambda: [])
    order = ['Benchmark', 'Progress', 'ETC', args.dir]

    table = {
        'Benchmark': '<0',
        'Progress':  '>12',
        args.dir:    f'>{len(args.dir) + 4}',
        'ETC':       '>11'
    }

    # Set spacing for benchmark table cell, by peeking at file names
    for file in os.listdir(args.dir):
        if file.endswith(".log"):
            bench = file.replace('.log', '')
            if len(bench) > int(table['Benchmark'][1:]):
                table['Benchmark'] = f'<{len(bench)}'
    
    # Parse stats csv, which contains real icp values
    if args.stat != '':
        table['Real'] = '>8'
        order.append('Real')

        stat_csv = pd.read_csv(args.stat)
        for i in stat_csv.iterrows():
            stats[i[1]['Bench']] = i[1]['IPC']

    # Parse compare args, building compare dict
    if len(args.compare) > 0:
        for comp in args.compare:
            table[comp] = f'>{len(comp) + 4}'
            order.append(comp)

            for file in os.listdir(comp):
                if file.endswith(".log"):
                    compare[comp].append(file)

    # Build output lines
    lines = []
    for file in os.listdir(args.dir):
        if file.endswith(".log"):
            bench = file.replace('.log', '')

            # Get results
            result = dict([ (key, '---') for key in order ])
            result['Benchmark'] = bench
            result = get_result(args.dir + '/' + file, result)
            if 'IPC' in result:
                result[args.dir] = result.pop('IPC')

            # Add real ipc values from "stats"
            if bench in stats:
                result['Real'] = f'{stats[bench]:.3f}'

            # Add compare ipc values from "compare"
            for comp, comp_files in compare.items():
                if file in comp_files:
                    compare_result = get_result(comp + '/' + file)
                    result[comp] = compare_result['IPC']

            # Build table line
            line = ''.join([ f'{result[field]:{table[field]}}' for field in order ])

            if result['Progress'] == 'DONE':
                line = f'{bcolors.OKGREEN}{line}{bcolors.ENDC}'

            lines.append(line)

    header = ''.join([ f'{field:{table[field]}}' for field in order ])

    # Print result
    print(header)
    print('-' * len(header))
    print('\n'.join(sorted(lines)))


if __name__ == '__main__':
    main()
