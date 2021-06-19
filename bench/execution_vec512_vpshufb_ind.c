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

    asm volatile("vmovapd (%%rsp), %%zmm0" : : : "zmm0");
    asm volatile("vmovapd (%%rsp), %%zmm1" : : : "zmm1");
    asm volatile("vmovapd (%%rsp), %%zmm2" : : : "zmm2");
    asm volatile("vmovapd (%%rsp), %%zmm3" : : : "zmm3");
    asm volatile("vmovapd (%%rsp), %%zmm4" : : : "zmm4");
    asm volatile("vmovapd (%%rsp), %%zmm5" : : : "zmm5");
    asm volatile("vmovapd (%%rsp), %%zmm6" : : : "zmm6");
    asm volatile("vmovapd (%%rsp), %%zmm7" : : : "zmm7");

    asm volatile("pop %%rbx" : : : "rbx");

    for (i = 1; i <= repetitions; i++) {
        asm volatile("vpshufb %%zmm0, %%zmm0, %%zmm0" : : : "zmm0");
        asm volatile("vpshufb %%zmm1, %%zmm1, %%zmm1" : : : "zmm1");
        asm volatile("vpshufb %%zmm2, %%zmm2, %%zmm2" : : : "zmm2");
        asm volatile("vpshufb %%zmm3, %%zmm3, %%zmm3" : : : "zmm3");
        asm volatile("vpshufb %%zmm4, %%zmm4, %%zmm4" : : : "zmm4");
        asm volatile("vpshufb %%zmm5, %%zmm5, %%zmm5" : : : "zmm5");
        asm volatile("vpshufb %%zmm6, %%zmm6, %%zmm6" : : : "zmm6");
        asm volatile("vpshufb %%zmm7, %%zmm7, %%zmm7" : : : "zmm7");

        asm volatile("vpshufb %%zmm0, %%zmm0, %%zmm0" : : : "zmm0");
        asm volatile("vpshufb %%zmm1, %%zmm1, %%zmm1" : : : "zmm1");
        asm volatile("vpshufb %%zmm2, %%zmm2, %%zmm2" : : : "zmm2");
        asm volatile("vpshufb %%zmm3, %%zmm3, %%zmm3" : : : "zmm3");
        asm volatile("vpshufb %%zmm4, %%zmm4, %%zmm4" : : : "zmm4");
        asm volatile("vpshufb %%zmm5, %%zmm5, %%zmm5" : : : "zmm5");
        asm volatile("vpshufb %%zmm6, %%zmm6, %%zmm6" : : : "zmm6");
        asm volatile("vpshufb %%zmm7, %%zmm7, %%zmm7" : : : "zmm7");

        asm volatile("vpshufb %%zmm0, %%zmm0, %%zmm0" : : : "zmm0");
        asm volatile("vpshufb %%zmm1, %%zmm1, %%zmm1" : : : "zmm1");
        asm volatile("vpshufb %%zmm2, %%zmm2, %%zmm2" : : : "zmm2");
        asm volatile("vpshufb %%zmm3, %%zmm3, %%zmm3" : : : "zmm3");
        asm volatile("vpshufb %%zmm4, %%zmm4, %%zmm4" : : : "zmm4");
        asm volatile("vpshufb %%zmm5, %%zmm5, %%zmm5" : : : "zmm5");
        asm volatile("vpshufb %%zmm6, %%zmm6, %%zmm6" : : : "zmm6");
        asm volatile("vpshufb %%zmm7, %%zmm7, %%zmm7" : : : "zmm7");

        asm volatile("vpshufb %%zmm0, %%zmm0, %%zmm0" : : : "zmm0");
        asm volatile("vpshufb %%zmm1, %%zmm1, %%zmm1" : : : "zmm1");
        asm volatile("vpshufb %%zmm2, %%zmm2, %%zmm2" : : : "zmm2");
        asm volatile("vpshufb %%zmm3, %%zmm3, %%zmm3" : : : "zmm3");
        asm volatile("vpshufb %%zmm4, %%zmm4, %%zmm4" : : : "zmm4");
        asm volatile("vpshufb %%zmm5, %%zmm5, %%zmm5" : : : "zmm5");
        asm volatile("vpshufb %%zmm6, %%zmm6, %%zmm6" : : : "zmm6");
        asm volatile("vpshufb %%zmm7, %%zmm7, %%zmm7" : : : "zmm7");
    }

    asm volatile("push $0x0":::);
    asm volatile("vmovapd %%zmm0, (%%rsp)" : : : );
    asm volatile("mov (%%rsp), %0" : "=r"(count) : : );
    asm volatile("pop %%rbx" : : : "rbx");

    printf("%lf\n", count);

    asm volatile ("nop");
    asm volatile ("nop");
    asm volatile ("nop");

    exit(EXIT_SUCCESS);
}
