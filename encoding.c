#include <stdio.h>

int main(int argc, char *argv[]) {
  char s[100];
  scanf("%99s", s);
  char *p = s;
  while (*p != 0) {
    printf("%02x ", (unsigned char)*p);
    p++;
  }
  return 0;
}
