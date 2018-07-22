#include <stdio.h>
#include <stdlib.h>
#include <wait.h>
#include <sys/types.h>
#include <unistd.h>

#define READ_END 0
#define WRITE_END 1


int main(int argc, char **argv) {
    if (argc < 3) {
        fprintf(stderr, "Less number of arguments\n");
	exit(-1);
    }
    int pipe_fd[2];

    if (pipe(pipe_fd) == -1) {
    	fprintf(stderr, "Pipe creation failed\n");
	exit(-2);
    }

    pid_t pid = fork();
    
    if (pid == -1) {
    	fprintf(stderr, "Child process creation failed\n");
	exit(-3);
    }

    if (pid > 0) {
    	// Parent process
   	 FILE *fin;
	 fin = fopen(argv[1], "rb");
	 
	 close(pipe_fd[READ_END]);
	 char buffer[10];

	 while (fread(buffer, sizeof(char), 9, fin) != 0) {
	     //printf("%s", buffer);
	     write(pipe_fd[WRITE_END], buffer, 9);
	 }
    }
    else if (pid == 0) {
    	// Child process
    	FILE *fout;
	char buffer[10];
	// fout = fopen(argv[2], "wb");
	close(pipe_fd[WRITE_END]);

	while (read(pipe_fd[READ_END], buffer, 9))
	    printf("%s", buffer);
    }

    return 0;
}
