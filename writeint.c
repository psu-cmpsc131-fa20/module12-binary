#include <stdio.h>

int main(int argc, char *argv[]) {
  FILE *output = fopen(argv[1], "wb");
  int numbers[100];
  for (int i = 0; i < 100; i++) {
    numbers[i] = -i;
  }
  fwrite(numbers, sizeof(int), 100, output);
  fclose(output);
  return 0;
}
