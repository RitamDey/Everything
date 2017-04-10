/**
 * Created by sTux
 * Dated April 5th, 2017
 * Standard: C11 with GNU extensions
 * Compile Flags: -std=gnu11 -Wall -l pthread -ggdb
**/

#include "stack/stack.h"
#include <pthread.h>
#define THREADS 5


pthread_cond_t cond;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
stack_t *stack;


void producer(void *arg) {
    pthread_mutex_lock(&mutex);
    char str[100];
    printf("%s", str);
    push(&stack, str);
    pthread_mutex_unlock(&mutex);
}


void consumer(void *arg) {
    pthread_mutex_lock(&mutex);
    char *str = NULL;
    pop(&str);
    printf("Popped %s\n", str);
    pthread_mutex_unlock(&mutex);
}


int main() {
    pthread_t producers[5], consumers[5];

    for(int i=0; i<5; ++i) {
        pthread_create(&producers[i], NULL, producer, NULL);
        pthread_create(&consumers[i], NULL, consumer, NULL);
    }

    for()
}
