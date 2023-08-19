// gcc day1-2.c -o day1-2 && ./day1-2

#include <stdio.h>
#include <string.h>

int day1_1() {
  int a, b, count=0;
  FILE *f = fopen("./input2.csv", "r");
  fscanf(f, "%d", &b);
  while(fscanf(f, "%d", &a) == 1) {
    if(a>b) count++;
    // printf("a %d b %d count %d\n", a,b,count);
    b=a;
  }
  fclose(f);
  return count;
}

int main() {
  int a, b, c;
  FILE *f1 = fopen("./input.csv", "r");
  FILE *f2 = fopen("./input2.csv", "w");
  fscanf(f1, "%d", &c);
  fscanf(f1, "%d", &b);
  while(fscanf(f1, "%d", &a) == 1) {
    fprintf(f2, "%d\n", a+b+c);
    c=b;
    b=a;
  }
  fclose(f1);
  fclose(f2);
  printf("%d\n", day1_1());
  return 0;
}
