#include <stdio.h>
#include <malloc.h>


typedef struct stack_t {
    int data;
    struct stack *next, *prev;
} stack_t;


typedef enum bool {
    false, true;
} bool;


stack_t *stack;
int max_cost;


bool add(int data) {
    ;
}


void remove() {
}


int main() {
    int n, cmds;
    scanf("%d", &n);
    int harry_bag[n];

    for(int i=0; i<n; ++i)
        scanf("%d", harry_bag[i]);

    for(int i=0; i<cmds; ++i) {

    }
