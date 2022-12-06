// gcc -Wall part1.c -o part1 -lm; ./part1; rm part1

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {
    char repeated;
    int len, sum=0;
    char str[5000];
    FILE* ptr = fopen("input.txt", "r");
    
    while (fgets(str, 5000, ptr)) {
        len = strlen(str);
        for (int i=0; i<len/2; i++) {
            if (strchr(&str[len/2], str[i]) != NULL) {
                repeated = str[i];
                break;
            }
        }
        printf("%c (%d) - %s\n", repeated, repeated, str);
        if (repeated >= 65 && repeated <= 90) {
            // A to Z
            sum += repeated - 65 + 27;
        } else if (repeated >= 97 && repeated <= 122) {
            // a to z
            sum += repeated - 97 + 1;
        }
    }
    fclose(ptr);
    printf("\ntotal: %d\n\n", sum);
}
