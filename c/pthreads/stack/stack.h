#ifndef PTHREADS_STACK_H
#define PTHREADS_STACK_H

#include <malloc.h>
#include <string.h>

typedef enum bool {
    false, true
} bool;


typedef struct stack_t {
    char *data;
    struct stack_t *next;
    struct stack_t *prev;
}stack_t ;


void init(stack_t **pStack, char *data);
void push(stack_t **stack, char *data);
void pop(char **ret);

#endif //PTHREADS_STACK_H