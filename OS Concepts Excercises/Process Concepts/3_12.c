/* Creating a zombie process */
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <time.h>


int main() {
  /**
   * A zombie process is a process which a process which has exited but its 
   * parent has called wait yet, thereby keeping the process entry table entry
   * intact for the defunct process.
   *
   * NOTE: A orphan process is a running process whose parent has exited and has
   * now been adopted by `init`
   **/
  pid_t child = fork();

  if (child == -1)
    printf("Child forking failed\n");

  else if (child == 0) {
    printf("In the child\n");
    printf("Exiting the child\n");
  }

  else {
    // Sleeping 10 seconds assures that the zombie exists in the system for
    // atleast 10 seconds before the parent call `wait()` on it to release PID
    // entries
    sleep(10);
    int child_status;
    child = wait(&child_status);
    printf("Child %d exited with code %d\n", child, child_status);
  }

  return 0;
}
