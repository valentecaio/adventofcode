// gcc -Wall part2.c -o part2 -lm; ./part2; rm part2

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXSIZE 255
#define STACKS 10

// stacks[9] is a temporary stack
char **stacks; // matrix, STACKS x MAXSIZE
int tops[10] = {2, 7, 4, 3, 6, 5, 7, 7, 6, -1}; // stack sizes

char pop(int sid) {
    char data;
    data = stacks[sid][tops[sid]];
    tops[sid] = tops[sid] - 1;
    return data;
}

void push(char data, int sid) {
    tops[sid] = tops[sid] + 1;
    stacks[sid][tops[sid]] = data;
}

void print_stacks() {
    for (int i=0; i<STACKS; i++) {
        printf("stack %d: ", i+1);
        for (int j=0; j<=tops[i]; j++) {
            printf("%c, ", stacks[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int times, from, to;
    // same as input.txt but skipping the first 10 lines
    FILE* ptr = fopen("input_mod.txt", "r");

    // allocate stacks
    stacks = (char**) malloc(STACKS*MAXSIZE*sizeof(char));
    for (int i=0;i<STACKS;i++) {
        stacks[i] = (char*) malloc(MAXSIZE*sizeof(int));
    }

    // init stacks
    strcpy(stacks[0], "WRF");
    strcpy(stacks[1], "THMCDVWP");
    strcpy(stacks[2], "PMZNL");
    strcpy(stacks[3], "JCHR");
    strcpy(stacks[4], "CPGHQTB");
    strcpy(stacks[5], "GCWLFZ");
    strcpy(stacks[6], "WVLQZJGC");
    strcpy(stacks[7], "PNRFWTVC");
    strcpy(stacks[8], "JWHGRSV");
    printf("\nINITIAL STACKS:\n");
    print_stacks();

    while (fscanf(ptr, "move %d from %d to %d\n", &times, &from, &to) == 3) {
        // push values to temp stack (stack[9]) and then back on the new stack
        printf("\nmove %d from %d to %d:\n", times, from, to);
        for (int i=0; i<times; i++, push(pop(from-1), 9));
        for (int i=0; i<times; i++, push(pop(9), to-1));
        print_stacks();
    }

    printf("\nfinal results: ");
    for (int i=0; i<STACKS; printf("%c", pop(i++)));
    printf("\n");

    for (int i=0; i<STACKS; free(stacks[i++]));
    free(stacks);
    fclose(ptr);
    return 0;
}