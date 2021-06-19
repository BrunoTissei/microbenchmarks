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

#define MIDDLE

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

    asm volatile("mov %0, %%rcx" : "=r"(repetitions) : "0"(repetitions));

    asm volatile("mov $1, %r8d");
    asm volatile("mov $1, %r9d");
    asm volatile("mov $1, %r10d");
    asm volatile("mov $1, %r11d");
    asm volatile("mov $1, %r12d");
    asm volatile("mov $1, %r13d");
    asm volatile("mov $1, %r14d");
    asm volatile("mov $1, %r15d");

    asm volatile ("nop");
    asm volatile ("nop");
    asm volatile ("nop");

    asm volatile("mov $1, %rbx");
    asm volatile("mov $0, %edx");
    asm volatile("loop:");
        asm volatile("mov $1, %rax");

        asm volatile("idiv %r8d");
        MIDDLE
        asm volatile("idiv %r9d");
        MIDDLE
        asm volatile("idiv %r10d");
        MIDDLE
        asm volatile("idiv %r11d");
        MIDDLE
        asm volatile("idiv %r12d");
        MIDDLE
        asm volatile("idiv %r13d");
        MIDDLE
        asm volatile("idiv %r14d");
        MIDDLE
        asm volatile("idiv %r15d");

        MIDDLE
        asm volatile("idiv %r8d");
        MIDDLE
        asm volatile("idiv %r9d");
        MIDDLE
        asm volatile("idiv %r10d");
        MIDDLE
        asm volatile("idiv %r11d");
        MIDDLE
        asm volatile("idiv %r12d");
        MIDDLE
        asm volatile("idiv %r13d");
        MIDDLE
        asm volatile("idiv %r14d");
        MIDDLE
        asm volatile("idiv %r15d");

        MIDDLE
        asm volatile("idiv %r8d");
        MIDDLE
        asm volatile("idiv %r9d");
        MIDDLE
        asm volatile("idiv %r10d");
        MIDDLE
        asm volatile("idiv %r11d");
        MIDDLE
        asm volatile("idiv %r12d");
        MIDDLE
        asm volatile("idiv %r13d");
        MIDDLE
        asm volatile("idiv %r14d");
        MIDDLE
        asm volatile("idiv %r15d");

        MIDDLE
        asm volatile("idiv %r8d");
        MIDDLE
        asm volatile("idiv %r9d");
        MIDDLE
        asm volatile("idiv %r10d");
        MIDDLE
        asm volatile("idiv %r11d");
        MIDDLE
        asm volatile("idiv %r12d");
        MIDDLE
        asm volatile("idiv %r13d");
        MIDDLE
        asm volatile("idiv %r14d");
        MIDDLE
        asm volatile("idiv %r15d");

    asm volatile("add $1, %rbx");
    asm volatile("cmp %rcx, %rbx");
    asm volatile("jne loop");

    asm volatile ("nop");
    asm volatile ("nop");
    asm volatile ("nop");

    // printf("%lu\n", count0 + count1 + count2 + count3 + count4 + count5 + count6 + count7);
    exit(EXIT_SUCCESS);
}
