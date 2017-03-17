#include <stdio.h>
#include <pthread.h>  // -lpthread needs to be passed to compile 

#define MAX_THREADS 5


void *hello(void *tid){
    printf("Hello from thread %ld", *(long *)tid);
    pthread_exit(NULL); // To indicate that the thread executed successfully
}

int main(){
    pthread_t threads[MAX_THREADS];
    int exit_code;
    for(int n=0; n < MAX_THREADS; ++n){
        /**
         * pthread_create() creates or init's a new thread 
         * Arguments are the address of thread variable, here address of the position in array
         * Thread's attributes, here NULL which means default behaviour
         *The third argument is the callback that would be runned by all threads
         *The last arguments are the arguments to be passed to the callback
         **/
        exit_code = pthread_create(&threads[n], NULL, hello, (void *)&n);
        if(exit_code){
            printf("Thread creation failed with %d exit code", exit_code);
            pthread_exit((void *)&exit_code);
        }
    }

    for(int n=0; n < MAX_THREADS; ++n){
        pthread_join(threads[n], NULL);
    }
    pthread_exit(NULL);
}

