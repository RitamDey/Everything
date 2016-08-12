#include <stdio.h>

int main(int argc, char const *argv[]) {
    if(argc == 1)
        printf("Hello World\n");
    else
    {
        *argv++;
        for (int a=2;a<=argc;a++,*argv++) {
            printf("Hello %s\n",*argv);
        }
    }
    return 0;
}
