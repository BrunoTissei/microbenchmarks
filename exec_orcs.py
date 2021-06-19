#!/usr/bin/env python3

import os
import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--trace-path',
                        type = str,
                        action = 'store',
                        required = True,
                        help = 'Path to directory with trace files')

    parser.add_argument('--orcs-path',
                        type = str,
                        action = 'store',
                        required = True,
                        help = 'Path to OrCS\'s root directory')

    parser.add_argument('--logs-path',
                        type = str,
                        action = 'store',
                        required = True,
                        help = 'Path to result logs directory')

    parser.add_argument('--num-cpu',
                        type = int,
                        action = 'store',
                        default = 1,
                        required = False,
                        help = 'Number of concurrent processes')

    return parser.parse_args()

def main():
    args = parse_args()

    logs_path = os.path.abspath(args.logs_path)
    orcs_path = os.path.abspath(args.orcs_path)
    trace_path = os.path.abspath(args.trace_path)
    orcs_config_path = f'{orcs_path}/configuration_files/skylake.cfg'
    
    executables = []
    for file in os.listdir(trace_path):
        if 'dyn.out.gz' in file:
            name = file.replace('.tid0.dyn.out.gz', '')
            executables.append({
                'trace': f'{trace_path}/{name}',
                'result': f'{logs_path}/{name}.log'
            })

    commands = [ f'./orcs -c {orcs_config_path} -t {i["trace"]} > {i["result"]}' for i in executables ]


    lines = []
    step = (len(commands) - 1) // args.num_cpu + 1
    for i in range(0, len(commands), step):
        lines.append(' && '.join(commands[i:i+step]))

    command = ' & '.join(lines) + ' & wait &'

    os.system(f'mkdir -p {logs_path}')
    os.system(f'cd {orcs_path}; {command}')

if __name__ == '__main__':
    main()
