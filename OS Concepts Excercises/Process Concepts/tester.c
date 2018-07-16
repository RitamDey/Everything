#include <stdio.h>
#include "pid.h"


int main() {
  if (allocate_map() == -1) {
    printf("Map allocation failed\n");
    return -1;
  }

  for (int i=1; i <= 300; ++i)
    printf("Allocated %d\n", allocate_pid());

  release_pid(500);

  printf("Allocated %d\n", allocate_pid());

  return 0;
}
