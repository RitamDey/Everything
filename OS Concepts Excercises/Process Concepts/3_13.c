#include <malloc.h>
#include "pid.h"

#define MIN_PID 300
#define MAX_PID 5000


short *map;
short curr_pid;


int allocate_map(void) {
  map = (short *)calloc(MAX_PID - MIN_PID, sizeof(short));
  if (map == NULL)
    return -1;
  curr_pid = 300;

  return 1;
}


int allocate_pid(void) {
  /*
   * Allocates a PID for a requesting process. It first checks if any PID is
   * free to be allocated. If so then it allocates the PID and looks for the
   * next empty PID in the table
   */
  if (curr_pid >= MAX_PID)
    return -1;

  int pid = curr_pid;

  map[pid - 300] = 1;

  for (; curr_pid < MAX_PID && map[curr_pid - 300] != 0; curr_pid++);

  return pid;
}


void release_pid(int pid) {
  /*
   * Releases the given PID in the map. It then checks if the given PID has
   * a value lower than of the current empty PID. If so track this empty to
   * allocate it in the next allocation call
   */
  map[pid - 300] = 0;

  if (pid < curr_pid)
    curr_pid = pid;
}
