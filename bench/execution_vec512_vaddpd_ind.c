/*
 * Copyright (C) 2014  Marco Antonio Zanata Alves (mazalves at inf.ufrgs.br)
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

// =============================================================================
uint64_t string_to_uint64(char *string) {
    uint64_t result = 0;
    char c;

    for (  ; (c = *string ^ '0') <= 9 && c >= 0; ++string) {
        result = result * 10 + c;
    }
    return result;
};

// =============================================================================
int main (int argc, char *argv[]) {
    uint64_t repetitions;
    if(argc == 2) {
        repetitions = string_to_uint64(argv[1]);
    }
    else {
        printf("Please provide the number of repetitions.\n");
        exit(EXIT_FAILURE);
    }

    uint64_t i = 0;
    double count = 0;
    double in = 0.00;

    asm volatile ("nop");
    asm volatile ("nop");
    asm volatile ("nop");

    asm volatile("push %0"::"r"(in):);

    asm volatile("vsubpd %%zmm0, %%zmm0, %%zmm0" : : : "zmm0");
    asm volatile("vsubpd %%zmm1, %%zmm1, %%zmm1" : : : "zmm1");
    asm volatile("vsubpd %%zmm2, %%zmm2, %%zmm2" : : : "zmm2");
    asm volatile("vsubpd %%zmm3, %%zmm3, %%zmm3" : : : "zmm3");
    asm volatile("vsubpd %%zmm4, %%zmm4, %%zmm4" : : : "zmm4");
    asm volatile("vsubpd %%zmm5, %%zmm5, %%zmm5" : : : "zmm5");
    asm volatile("vsubpd %%zmm6, %%zmm6, %%zmm6" : : : "zmm6");
    asm volatile("vsubpd %%zmm7, %%zmm7, %%zmm7" : : : "zmm7");
    asm volatile("vsubpd %%zmm8, %%zmm8, %%zmm8" : : : "zmm8");
    asm volatile("vsubpd %%zmm9, %%zmm9, %%zmm9" : : : "zmm9");
    asm volatile("vsubpd %%zmm10, %%zmm10, %%zmm10" : : : "zmm10");
    asm volatile("vsubpd %%zmm11, %%zmm11, %%zmm11" : : : "zmm11");
    asm volatile("vsubpd %%zmm12, %%zmm12, %%zmm12" : : : "zmm12");
    asm volatile("vsubpd %%zmm13, %%zmm13, %%zmm13" : : : "zmm13");
    asm volatile("vsubpd %%zmm14, %%zmm14, %%zmm14" : : : "zmm14");
    asm volatile("vsubpd %%zmm15, %%zmm15, %%zmm15" : : : "zmm15");
    asm volatile("vsubpd %%zmm16, %%zmm16, %%zmm16" : : : "zmm16");
    asm volatile("vsubpd %%zmm17, %%zmm17, %%zmm17" : : : "zmm17");
    asm volatile("vsubpd %%zmm18, %%zmm18, %%zmm18" : : : "zmm18");
    asm volatile("vsubpd %%zmm19, %%zmm19, %%zmm19" : : : "zmm19");
    asm volatile("vsubpd %%zmm20, %%zmm20, %%zmm20" : : : "zmm20");
    asm volatile("vsubpd %%zmm21, %%zmm21, %%zmm21" : : : "zmm21");
    asm volatile("vsubpd %%zmm22, %%zmm22, %%zmm22" : : : "zmm22");
    asm volatile("vsubpd %%zmm23, %%zmm23, %%zmm23" : : : "zmm23");
    asm volatile("vsubpd %%zmm24, %%zmm24, %%zmm24" : : : "zmm24");
    asm volatile("vsubpd %%zmm25, %%zmm25, %%zmm25" : : : "zmm25");
    asm volatile("vsubpd %%zmm26, %%zmm26, %%zmm26" : : : "zmm26");
    asm volatile("vsubpd %%zmm27, %%zmm27, %%zmm27" : : : "zmm27");
    asm volatile("vsubpd %%zmm28, %%zmm28, %%zmm28" : : : "zmm28");
    asm volatile("vsubpd %%zmm29, %%zmm29, %%zmm29" : : : "zmm29");
    asm volatile("vsubpd %%zmm30, %%zmm30, %%zmm30" : : : "zmm30");
    asm volatile("vsubpd %%zmm31, %%zmm31, %%zmm31" : : : "zmm31");


    asm volatile("pop %%rbx" : : : "rbx");

    for (i = 1; i <= repetitions; i++) {
        asm volatile("vaddpd %%zmm0, %%zmm0, %%zmm0" : : : "zmm0");
        asm volatile("vaddpd %%zmm1, %%zmm1, %%zmm1" : : : "zmm1");
        asm volatile("vaddpd %%zmm2, %%zmm2, %%zmm2" : : : "zmm2");
        asm volatile("vaddpd %%zmm3, %%zmm3, %%zmm3" : : : "zmm3");
        asm volatile("vaddpd %%zmm4, %%zmm4, %%zmm4" : : : "zmm4");
        asm volatile("vaddpd %%zmm5, %%zmm5, %%zmm5" : : : "zmm5");
        asm volatile("vaddpd %%zmm6, %%zmm6, %%zmm6" : : : "zmm6");
        asm volatile("vaddpd %%zmm7, %%zmm7, %%zmm7" : : : "zmm7");

        asm volatile("vaddpd %%zmm8, %%zmm8, %%zmm8" : : : "zmm8");
        asm volatile("vaddpd %%zmm9, %%zmm9, %%zmm9" : : : "zmm9");
        asm volatile("vaddpd %%zmm10, %%zmm10, %%zmm10" : : : "zmm10");
        asm volatile("vaddpd %%zmm11, %%zmm11, %%zmm11" : : : "zmm11");
        asm volatile("vaddpd %%zmm12, %%zmm12, %%zmm12" : : : "zmm12");
        asm volatile("vaddpd %%zmm13, %%zmm13, %%zmm13" : : : "zmm13");
        asm volatile("vaddpd %%zmm14, %%zmm14, %%zmm14" : : : "zmm14");
        asm volatile("vaddpd %%zmm15, %%zmm15, %%zmm15" : : : "zmm15");
                                                                    
        asm volatile("vaddpd %%zmm16, %%zmm16, %%zmm16" : : : "zmm16");
        asm volatile("vaddpd %%zmm17, %%zmm17, %%zmm17" : : : "zmm17");
        asm volatile("vaddpd %%zmm18, %%zmm18, %%zmm18" : : : "zmm18");
        asm volatile("vaddpd %%zmm19, %%zmm19, %%zmm19" : : : "zmm19");
        asm volatile("vaddpd %%zmm20, %%zmm20, %%zmm20" : : : "zmm20");
        asm volatile("vaddpd %%zmm21, %%zmm21, %%zmm21" : : : "zmm21");
        asm volatile("vaddpd %%zmm22, %%zmm22, %%zmm22" : : : "zmm22");
        asm volatile("vaddpd %%zmm23, %%zmm23, %%zmm23" : : : "zmm23");
                                                                    
        asm volatile("vaddpd %%zmm24, %%zmm24, %%zmm24" : : : "zmm24");
        asm volatile("vaddpd %%zmm25, %%zmm25, %%zmm25" : : : "zmm25");
        asm volatile("vaddpd %%zmm26, %%zmm26, %%zmm26" : : : "zmm26");
        asm volatile("vaddpd %%zmm27, %%zmm27, %%zmm27" : : : "zmm27");
        asm volatile("vaddpd %%zmm28, %%zmm28, %%zmm28" : : : "zmm28");
        asm volatile("vaddpd %%zmm29, %%zmm29, %%zmm29" : : : "zmm29");
        asm volatile("vaddpd %%zmm30, %%zmm30, %%zmm30" : : : "zmm30");
        asm volatile("vaddpd %%zmm31, %%zmm31, %%zmm31" : : : "zmm31");
    }

    asm volatile("push $0x0":::);
    asm volatile("mov (%%rsp), %0" : "=r"(count) : : );
    asm volatile("pop %%rbx" : : : "rbx");

    printf("%lf\n", count);

    asm volatile ("nop");
    asm volatile ("nop");
    asm volatile ("nop");

    exit(EXIT_SUCCESS);
}
