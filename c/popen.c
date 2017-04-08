#include <stdio.h>
#include <stdlib.h>

/**
  * popen, pclose - pipe stream to or from a process
  * #include <stdio.h>
  * FILE *popen(const char *command, const char *type);
  * int pclose(FILE *stream);
  * popen() executes a shell command and passes it to a FILE stream
  * pclose() close the FILE stream
**/

int main() {
    FILE *fp;
    char path[1035];

    /* Open the command for reading */
    // fp = popen("/bin/ls", "/etc/", "r");
    fp = popen(
        "python3.6 -c 'from random import choice, randint;from string import ascii_letters, digits; print(*[choice(ascii_letters+digits) for _ in range(randint(10 ,20))], sep=str())'",
        "r");
    if(fp == NULL) {
        printf("Failed to run the command");
        exit(1);
    }

    // /* Read the output a line a time and output it */
    // while(fgets(path, sizeof(path)-1, fp) != NULL) {
    //     printf("%s\n", path);
    // }

    fgets(path, 1000, fp);
    printf("%s\n", path);

    pclose(fp);
    return 0;
}