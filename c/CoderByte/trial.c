#include <stdio.h>
#include<strings.h>

char str[200];

void FirstReverse() {
  printf("%s", strrev(str));
}

int main(void) {
  FirstReverse(gets(stdin));
  return 0;
}
