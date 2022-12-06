// gcc -Wall part2.c -o part2 -lm; ./part2; rm part2

#include <stdio.h>
#define N 14

int has_duplicate(char *v, int n) {
    for (int i=0; i<n-1; i++)
        for (int j=i+1; j<n; j++)
            if (v[i] == v[j])
                return 1;
    return 0;
}

int main() {
    char v[N];
    int i;
    FILE* ptr = fopen("input.txt", "r");
    for(i=0; i<N || has_duplicate(v, N); fscanf(ptr, "%c", &v[i++%N]));
    printf("\nfinal answer: %d\n", i);
    fclose(ptr);
    return 0;
}
