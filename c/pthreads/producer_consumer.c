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
pthread_mutex_t mutex;
stack_t *stack;


void producer() {
    pthread_mutex_lock(&mutex);
    char str[100];
    printf("%s", str);
    push(&stack, str);
    pthread_mutex_unlock(&mutex);
}


void consumer() {
    pthread_mutex_lock(&mutex);
    char *str = NULL;
    pop(&str);
    printf("Popped %s\n", str);
    pthread_mutex_unlock(&mutex);
}


int main() {
}