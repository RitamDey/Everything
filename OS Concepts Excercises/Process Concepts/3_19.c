#include <unistd.h>
#include <sys/types.h>
#include <wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define READ_END 0  // Denotes the read end of the pipe
#define WRITE_END 1  // Denotes the write end of the pipe


void convert(char *s) {
    while (*s != '\0') {
        if (islower(*s))
	    *s = toupper(*s);
	else
	    *s = tolower(*s);
	s++;
    }
}


int main() {
    char s[200];

    scanf("%[^\n]s", s);
    fflush(stdin);

    int length = strlen(s);

    // We need a 2-element array to hold the file descriptors for the pipe's read and write end
    int pipe_send_fd[2];
    int pipe_read_fd[2];

    pid_t pid;

    if (pipe(pipe_send_fd) == -1) {
        printf("Send pipe creation failed.\n");
	exit(-1);
    }

    if (pipe(pipe_read_fd) == -1) {
    	printf("Read pipe creation failed.\n");
	exit(-1);
    }

    pid = fork();

    if (pid == -1) {
    	printf("Child creation failed.\n");
	exit(-1);
    }

    if (pid > 0) {
        // Parent process

	// Close the unused end of the pipes
        close(pipe_send_fd[READ_END]);
	close(pipe_read_fd[WRITE_END]);

	// First wite out the message to the pipe and the wait util the child finishes
	write(pipe_send_fd[WRITE_END], s, length + 1);
	wait(NULL);

	// By now, the child has written the converted message, read it and print it out
	read(pipe_read_fd[READ_END], s, length + 1);

	// Also close the pipes entirely.
	close(pipe_send_fd[WRITE_END]);
	close(pipe_read_fd[READ_END]);

	puts(s);
    }
    else if (pid == 0) {
        // Child process

	// Close the unused ends of the pipes
    	close(pipe_send_fd[WRITE_END]);
	close(pipe_read_fd[READ_END]);

	// Read the data sentin by the parent process
	read(pipe_send_fd[READ_END], s, length + 1);

	convert(s);  // Convert the message

	// Write out the converted message
	write(pipe_read_fd[WRITE_END], s, strlen(s) + 1);

	// Close the pipes completely
	close(pipe_send_fd[READ_END]);
	close(pipe_read_fd[WRITE_END]);
   }

   return 0;
}
