// gcc day3-1.c -lm -o day3-1 && ./day3-1

#include <stdio.h>
#include <math.h>

void print_vector(int *v, int n) {
  printf("[");
  for(int j=0; j<n; j++) {
    printf(" %d", v[j]);
  }
  printf(" ]\n");
}

int main() {
  int i, count[12], tot=0, gama=0, epsilon=0;
  char v[12];

  // init
  for(i=0; i<12; count[i]=0, i++);

  // read file and fill count
  FILE *f = fopen("./input.txt", "r");
  while(fscanf(f, "%s", v) == 1) {
    for(i=0; i<12; i++) {
      count[i] += (v[i] == '1') ? 1 : 0;
    }
    printf("%s\n", v);
    tot++;
  }
  fclose(f);

  // some prints
  printf("count: ");
  print_vector(count, 12);
  printf("tot = %d\n", tot);

  // cast counters to ones and zeroes
  for(i=0; i<12; i++) {
    count[i] = (count[i] > (tot/2)) ? 1 : 0;
  }
  printf("count: ");
  print_vector(count, 12);

  // find gama and epsilon, and final results
  for(i=0; i<12; i++) {
    gama += count[i] * (int)(pow(2, 11-i));
    epsilon += !count[i] * (int)(pow(2, 11-i));
    // printf("gama: %d (0x%x)\n", gama, gama);
    // printf("epsilon: %d (0x%x)\n", epsilon, epsilon);
  }
  printf("gama: %d (0x%x)\n", gama, gama);
  printf("epsilon: %d (0x%x)\n", epsilon, epsilon);
  printf("gama * epsilon: %d (0x%x)\n", gama*epsilon, gama*epsilon);
  return 0;
}
