/**
 * Created by sTux
 * Dated April 5, 2017
 * C Standard: C11 with GNU extensions
 * Compile Flags: -std=gnu11 -Wall -g -l pthread
 * Topic Covered: Basic usage of pthreads and getting pid and tid
**/

#include <stdio.h>
#include <pthread.h>  // For the pthread_t, pthread_self(), pthread_join(), pthread_create()
#include <unistd.h>  // For the getpid() and pid_t


void *hello(void *id){
    // This gets the process id returned by pthread_create
    pid_t tid = (pid_t) pthread_self();
    // Used to get the Linux process id
    pid_t pid = getpid();

    printf("Hello from Thread %u with Thread ID %u of Program %d\n", *(int *)id, tid, pid);
    return NULL;
}


int main(){
    pthread_t threads[5];
    int arr[] = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; ++i) {
        // Create threads with default properties and hello callback and its arguments
        pthread_create(&threads[i], NULL, hello, &arr[i]);
    }

    for (int j = 0; j < 5; ++j) {
        // Makes the process wait till all threads have died
        pthread_join(threads[j], NULL);
    }

    return 0;
}
