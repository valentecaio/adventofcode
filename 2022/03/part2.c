// gcc -Wall part2.c -o part2 -lm; ./part2; rm part2

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {
    char repeated;
    int sum=0;
    char str1[255], str2[255], str3[255];
    FILE* ptr = fopen("input.txt", "r");
    
    while (fgets(str1, 255, ptr)) {
        fgets(str2, 255, ptr);
        fgets(str3, 255, ptr);
        for (int i=0; i<strlen(str1); i++) {
            if (strchr(str2, str1[i]) != NULL && strchr(str3, str1[i]) != NULL) {
                repeated = str1[i];
                break;
            }
        }
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
