// gcc day1-1.c -o day1-1 && ./day1-1

#include <stdio.h>
#include <string.h>

int main() {
  int a, b, count=0;
  FILE *f = fopen("./input.csv", "r");
  fscanf(f, "%d", &b);
  while(fscanf(f, "%d", &a) == 1) {
    if(a>b) count++;
    b=a;
  }
  fclose(f);
  printf("%d\n", count);
  return 0;
}
