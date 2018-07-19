#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <wait.h>
#include <stdlib.h>


void pattern(int start) {
  printf("%d ", start);

  if (start == 1)
    return;
  else if (start%2) {
    start = 3 * start + 1;
    pattern(start);
  }
  else
    pattern(start/2);
}


int main(int argc, char **argv) {
  if (argc < 2) {
    printf("Not enough command-line arguments\n");
    return -1;
  }

  int num = atoi(argv[1]);
  if (num <= 0) {
    printf("Positive number needed\n");
    return -1;
  }

  pid_t child = fork();

  if (child == -1) {
    printf("Child fork failed\n");
    return -1;
  }

  else if (child == 0) {
    pattern(num);
    return 0;
  }

  else {
    wait(NULL);
    printf("\n");
  }
}
