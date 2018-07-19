// For shared memory and memory mapped files
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>  // For generic purpose
#include <stdlib.h> // For generic purpose
// For fork() and wait()
#include <sys/types.h>
#include <unistd.h>
#include <wait.h>
#include <string.h>  // For memcpy()


unsigned int collatz(int num) {
  if (num == 1)
    return 1;
  else if (num%2)
    return num + collatz(3 * num + 1);
  else
    return num + collatz(num/2);
}


int main(int argc, char **argv) {
  if (argc < 2) {
    fprintf(stderr, "Less number of arguments than required.\n");
    exit(-1);
  }

  int num = atoi(argv[1]);
  if (num <= 0) {
    fprintf(stderr, "Positive number required.\n");
    exit(-1);
  }

  pid_t child = fork();

  if (child == -1) {
    fprintf(stderr, "Child creation failed\n");
    exit(-1);
  }
  else if (child == 0) {
    unsigned int result = collatz(num);

    // Exclusively create a shared memory object in R\W mode with R\W access to the user
    int shm_fd = shm_open("result", O_CREAT | O_EXCL | O_RDWR, S_IRUSR | S_IWUSR);

    if (shm_fd == -1) {
    	fprintf(stderr, "Shared memory creation failed\n");
	exit(-2);
    }

    // Truncate the size of unlying shared memory object to the size of `unsigned int`
    ftruncate(shm_fd, sizeof(unsigned int));

    // Map the shared memory to a memory mapped file with Write permission. POSIX SHM needs only MAP_SHARED flag
    void *addr = mmap(NULL, sizeof(unsigned int), PROT_WRITE, MAP_SHARED, shm_fd, 0);

    // Copy the result 
    memcpy(addr, &result, sizeof(unsigned int));

    // Close the shared memory file descriptor and unlink the memory mapped file
    close(shm_fd);
    munmap(addr, sizeof(unsigned int));
  }
  else {
    wait(NULL);
    // Join shared memory with read-only permission
    int shm_fd = shm_open("result", O_RDONLY, S_IRUSR);
    if (shm_fd == -1) {
    	fprintf(stderr, "Shared memory linking failed\n");
	exit(-2);
    }

    // Map the file to the process's memory with only read permissions
    void *addr = mmap(NULL, sizeof(unsigned int), PROT_READ, MAP_SHARED, shm_fd, 0);

    // Cast the pointer as a `unsigned int` pointer and use it to print the result
    fprintf(stdout, "%u\n", *(unsigned int *)addr);

    // Close the SHM file descriptor, unmap the memory mapped file and ask OS to unlink and destroy the Shared Memory
    close(shm_fd);
    munmap(addr, sizeof(unsigned int));
    shm_unlink("result");
  }

  return 0;
}
