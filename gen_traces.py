#!/usr/bin/env python3

import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--trace-path',
                        type = str,
                        action = 'store',
                        required = True,
                        help = 'Path to directory where trace files will be saved')

    parser.add_argument('--orcs-path',
                        type = str,
                        action = 'store',
                        required = True,
                        help = 'Path to OrCS\'s root directory')

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

    return parser.parse_args()


def trace_gen(args, file, *params):
    orcs_path = os.path.abspath(args.orcs_path)
    trace_path = os.path.abspath(args.trace_path)

    os.system(f'{orcs_path}/trace_generator/pin -t {orcs_path}/trace_generator/extras/pinplay/bin/intel64/sinuca_tracer.so -trace intel64 -- ./bin/{file} {" ".join(map(str, params))}')

    name = f'{file}'
    if len(params) > 1:
        name += f'_{"_".join(map(str, params[1:]))}'

    os.system(f'mv output_trace.out.tid0.dyn.out.gz {trace_path}/{name}.out.tid0.dyn.out.gz')
    os.system(f'mv output_trace.out.tid0.mem.out.gz {trace_path}/{name}.out.tid0.mem.out.gz')
    os.system(f'mv output_trace.out.tid0.stat.out.gz {trace_path}/{name}.out.tid0.stat.out.gz')


def main():
    args = parse_args()

    trace_path = os.path.abspath(args.trace_path)
    os.system(f'mkdir -p {trace_path}')
    
    if args.type == 'control':
        trace_gen(args, 'control_complex',     1*10**6)
        trace_gen(args, 'control_conditional', 1*10**6)
        trace_gen(args, 'control_random',      1*10**6)   
        trace_gen(args, 'control_small_bbl',   1*10**6)
        trace_gen(args, 'control_switch',      1*10**6)

    elif args.type == 'dependency':
        trace_gen(args, 'dependency_chain1', 1*10**6)
        trace_gen(args, 'dependency_chain2', 1*10**6)
        trace_gen(args, 'dependency_chain3', 1*10**6)
        trace_gen(args, 'dependency_chain4', 1*10**6)
        trace_gen(args, 'dependency_chain5', 1*10**6)
        trace_gen(args, 'dependency_chain6', 1*10**6)

    elif args.type == 'execution_fp':
        trace_gen(args, 'execution_fp_addsd_ind',  1*10**6)
        trace_gen(args, 'execution_fp_divsd_ind',  1*10**6)
        trace_gen(args, 'execution_fp_maxsd_ind',  1*10**6)
        trace_gen(args, 'execution_fp_mulsd_ind',  1*10**6)
        trace_gen(args, 'execution_fp_pslld_ind',  1*10**6)
        trace_gen(args, 'execution_fp_pxor_ind',   1*10**6)
        trace_gen(args, 'execution_fp_shufpd_ind', 1*10**6)
        trace_gen(args, 'execution_fp_sqrtsd_ind', 1*10**6)

    elif args.type == 'execution_int':
        trace_gen(args, 'execution_int_add_ind',   1*10**6)
        trace_gen(args, 'execution_int_andn_ind',  1*10**6)
        trace_gen(args, 'execution_int_bextr_ind', 1*10**6)
        trace_gen(args, 'execution_int_div_ind',   1*10**6)
        trace_gen(args, 'execution_int_mul_ind',   1*10**6)
        trace_gen(args, 'execution_int_rcl_ind',   1*10**6)
        trace_gen(args, 'execution_int_shl_ind',   1*10**6)
        #tracegen execution_int_xor_ind     $((1*10**6))
        #tracegen execution_int_xchg_ind    $((1*10**6))

    elif args.type == 'execution_vec':
        trace_gen(args, 'execution_vec_dpps_ind',      1*10**6)
        trace_gen(args, 'execution_vec_vaddsd_ind',    1*10**6)
        trace_gen(args, 'execution_vec_vcvtsi2sd_ind', 1*10**6)
        trace_gen(args, 'execution_vec_vdivsd_ind',    1*10**6)
        trace_gen(args, 'execution_vec_vmulsd_ind',    1*10**6)
        trace_gen(args, 'execution_vec_vpsllvq_ind',   1*10**6)
        trace_gen(args, 'execution_vec_vshufps_ind',   1*10**6)
        trace_gen(args, 'execution_vec_vsqrtpd_ind',   1*10**6)
        trace_gen(args, 'execution_vec_vxorpd_ind',    1*10**6)

    elif args.type == 'execution_vec512':
        trace_gen(args, 'execution_vec512_vaddpd_ind',      1*10**6)
        trace_gen(args, 'execution_vec512_vdivpd_ind',      1*10**6)
        trace_gen(args, 'execution_vec512_vfmadd132pd_ind', 1*10**6)
        trace_gen(args, 'execution_vec512_vmulpd_ind',      1*10**6)
        trace_gen(args, 'execution_vec512_vpshufb_ind',     1*10**6)
        trace_gen(args, 'execution_vec512_vpsllvd_ind',     1*10**6)
        trace_gen(args, 'execution_vec512_vpxord_ind',      1*10**6)
        trace_gen(args, 'execution_vec512_vrsqrt14ps_ind',  1*10**6)

    elif args.type == 'memory':
        trace_gen(args, 'memory_load_dep', 4*2048, 65536//64)
        trace_gen(args, 'memory_load_dep', 4*1024, 131072//64)
        trace_gen(args, 'memory_load_dep', 4*512,  262144//64)
        trace_gen(args, 'memory_load_dep', 4*256,  524288//64)
        trace_gen(args, 'memory_load_dep', 4*128,  1048576//64)
        trace_gen(args, 'memory_load_dep', 4*64,   2097152//64)
        trace_gen(args, 'memory_load_dep', 4*32,   4194304//64)
        
        trace_gen(args, 'memory_load_ind', 16*512, 65536//64)
        trace_gen(args, 'memory_load_ind', 16*256, 131072//64)
        trace_gen(args, 'memory_load_ind', 16*128, 262144//64)
        trace_gen(args, 'memory_load_ind', 16*64,  524288//64)
        trace_gen(args, 'memory_load_ind', 16*32,  1048576//64)
        trace_gen(args, 'memory_load_ind', 16*16,  2097152//64)
        trace_gen(args, 'memory_load_ind', 16*8,   4194304//64)
        
        trace_gen(args, 'memory_store_ind', 16*512, 65536//64)
        trace_gen(args, 'memory_store_ind', 16*256, 131072//64)
        trace_gen(args, 'memory_store_ind', 16*128, 262144//64)
        trace_gen(args, 'memory_store_ind', 16*64,  524288//64)
        trace_gen(args, 'memory_store_ind', 16*32,  1048576//64)
        trace_gen(args, 'memory_store_ind', 16*16,  2097152//64)
        trace_gen(args, 'memory_store_ind', 16*8,   4194304//64)

if __name__ == '__main__':
    main()
