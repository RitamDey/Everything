/**
 * This simple example code creates 5 threads with the pthread_create() routine.
 * Each thread prints a "Hello World!" message, 
 * And then terminates with a call to pthread_exit().
**/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#define NUM_THREADS 5


void *PrintHello(void *threadid) {
    long tid;  // The argument is the id instead of the address to the id
    tid = (long)threadid;  // Convert the pointer arg to the value
    printf("Hello World!, It's me , thread %ld\n", tid);
    pthread_exit(NULL);
}


int main(int argc, char **argv) {
    pthread_t threads[NUM_THREADS];
    int rc;
    long t;
    for(t=0; t<NUM_THREADS; t++) {
        printf("In main: creating thread number %ld\n", t);

        /** 
         * pthread_create() just puts the unique thread id of the newly created thread
         * So just send it as the arg to the callback
        **/
        rc = pthread_create(&threads[t], NULL, PrintHello, (void *)t);
        if(rc) {
            printf("ERROR; return code from pthread_create(0 is %d\n", rc);
            exit(-1);
        }
    }
    
    pthread_exit(NULL);
}
