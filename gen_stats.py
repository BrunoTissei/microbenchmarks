#!/usr/bin/env python3

import os
import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--type',
                        type = str,
                        choices = [
                            'control',
                            'dependency',
                            'execution_fp',
                            'execution_int',
                            'execution_vec',
                            'execution_vec512',
                            'memory'
                        ],
                        action = 'store',
                        required = True,
                        help = 'Desired group of microbenchmarks')

    parser.add_argument('--output-file',
                        type = str,
                        action = 'store',
                        default = None,
                        required = False,
                        help = 'CSV output file for results')

    return parser.parse_args()


def stat_gen(args, file, *params):
    real = subprocess.check_output([
        f"""
        TEMP=$(mktemp .stats.XXXXXX.tmp) &&
        (sudo perf stat --repeat=1000 ./bin/{file} {" ".join(map(str, params))}) > $TEMP.log 2>&1 && 
        cat $TEMP.log | grep "insn per cycle" | awk \'{{ printf $4 }}\' &&
        rm $TEMP.log
        """
    ], shell=True).decode('utf-8').replace(',', '.')

    name = f'{file}'
    if len(params) > 1:
        name += f'_{"_".join(map(str, params[1:]))}'
    
    print(f'{name},{real}')
    if args.output_file != None:
        print(f'{name},{real}', file=open(args.output_file, "a"))


def main():
    args = parse_args()

    print('bench,IPC')
    if args.output_file != None:
        print('bench,IPC', file=open(args.output_file, "a"))

    if args.type == 'control':
        stat_gen(args, 'control_complex',     1*10**6)
        stat_gen(args, 'control_conditional', 1*10**6)
        stat_gen(args, 'control_random',      1*10**6)   
        stat_gen(args, 'control_small_bbl',   1*10**6)
        stat_gen(args, 'control_switch',      1*10**6)

    elif args.type == 'dependency':
        stat_gen(args, 'dependency_chain1', 1*10**6)
        stat_gen(args, 'dependency_chain2', 1*10**6)
        stat_gen(args, 'dependency_chain3', 1*10**6)
        stat_gen(args, 'dependency_chain4', 1*10**6)
        stat_gen(args, 'dependency_chain5', 1*10**6)
        stat_gen(args, 'dependency_chain6', 1*10**6)

    elif args.type == 'execution_fp':
        stat_gen(args, 'execution_fp_addsd_ind',  1*10**6)
        stat_gen(args, 'execution_fp_divsd_ind',  1*10**6)
        stat_gen(args, 'execution_fp_maxsd_ind',  1*10**6)
        stat_gen(args, 'execution_fp_mulsd_ind',  1*10**6)
        stat_gen(args, 'execution_fp_pslld_ind',  1*10**6)
        stat_gen(args, 'execution_fp_pxor_ind',   1*10**6)
        stat_gen(args, 'execution_fp_shufpd_ind', 1*10**6)
        stat_gen(args, 'execution_fp_sqrtsd_ind', 1*10**6)

    elif args.type == 'execution_int':
        stat_gen(args, 'execution_int_add_ind',   1*10**6)
        stat_gen(args, 'execution_int_andn_ind',  1*10**6)
        stat_gen(args, 'execution_int_bextr_ind', 1*10**6)
        stat_gen(args, 'execution_int_div_ind',   1*10**6)
        stat_gen(args, 'execution_int_mul_ind',   1*10**6)
        stat_gen(args, 'execution_int_rcl_ind',   1*10**6)
        stat_gen(args, 'execution_int_shl_ind',   1*10**6)
        #tracegen execution_int_xor_ind     $((1*10**6))
        #tracegen execution_int_xchg_ind    $((1*10**6))

    elif args.type == 'execution_vec':
        stat_gen(args, 'execution_vec_dpps_ind',      1*10**6)
        stat_gen(args, 'execution_vec_vaddsd_ind',    1*10**6)
        stat_gen(args, 'execution_vec_vcvtsi2sd_ind', 1*10**6)
        stat_gen(args, 'execution_vec_vdivsd_ind',    1*10**6)
        stat_gen(args, 'execution_vec_vmulsd_ind',    1*10**6)
        stat_gen(args, 'execution_vec_vpsllvq_ind',   1*10**6)
        stat_gen(args, 'execution_vec_vshufps_ind',   1*10**6)
        stat_gen(args, 'execution_vec_vsqrtpd_ind',   1*10**6)
        stat_gen(args, 'execution_vec_vxorpd_ind',    1*10**6)

    elif args.type == 'execution_vec512':
        stat_gen(args, 'execution_vec512_vaddpd_ind',     1*10**6)
        stat_gen(args, 'execution_vec512_vdivpd_ind',     1*10**6)
        stat_gen(args, 'execution_vec512_vmulpd_ind',     1*10**6)
        stat_gen(args, 'execution_vec512_vpshufb_ind',    1*10**6)
        stat_gen(args, 'execution_vec512_vpsllvd_ind',    1*10**6)
        stat_gen(args, 'execution_vec512_vpxord_ind',     1*10**6)
        stat_gen(args, 'execution_vec512_vrsqrt14ps_ind', 1*10**6)

    elif args.type == 'memory':
        stat_gen(args, 'memory_load_dep', 4*2048, 65536//64)
        stat_gen(args, 'memory_load_dep', 4*1024, 131072//64)
        stat_gen(args, 'memory_load_dep', 4*512,  262144//64)
        stat_gen(args, 'memory_load_dep', 4*256,  524288//64)
        stat_gen(args, 'memory_load_dep', 4*128,  1048576//64)
        stat_gen(args, 'memory_load_dep', 4*64,   2097152//64)
        stat_gen(args, 'memory_load_dep', 4*32,   4194304//64)
        
        stat_gen(args, 'memory_load_ind', 16*512, 65536//64)
        stat_gen(args, 'memory_load_ind', 16*256, 131072//64)
        stat_gen(args, 'memory_load_ind', 16*128, 262144//64)
        stat_gen(args, 'memory_load_ind', 16*64,  524288//64)
        stat_gen(args, 'memory_load_ind', 16*32,  1048576//64)
        stat_gen(args, 'memory_load_ind', 16*16,  2097152//64)
        stat_gen(args, 'memory_load_ind', 16*8,   4194304//64)
        
        stat_gen(args, 'memory_store_ind', 16*512, 65536//64)
        stat_gen(args, 'memory_store_ind', 16*256, 131072//64)
        stat_gen(args, 'memory_store_ind', 16*128, 262144//64)
        stat_gen(args, 'memory_store_ind', 16*64,  524288//64)
        stat_gen(args, 'memory_store_ind', 16*32,  1048576//64)
        stat_gen(args, 'memory_store_ind', 16*16,  2097152//64)
        stat_gen(args, 'memory_store_ind', 16*8,   4194304//64)

if __name__ == '__main__':
    main()
