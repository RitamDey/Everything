#include <stdio.h>
#include <malloc.h>


typedef struct queue {
    int data;
    struct queue *next;
    struct queue *prev;
} queue_t ;


queue_t *rear = NULL;
unsigned int len = 0;


queue_t *init(int data, queue_t *next, queue_t *prev) {
    queue_t *queue = (queue_t *)malloc(sizeof(queue_t));
    queue->data = data;
    queue->next = next;
    queue->prev = prev;
    if(rear == NULL)
        rear = queue;
    ++len;
    return queue;
}


void dequeue() {
    if(len == 0)
        printf("-1 0\n");
    else {
        int data = rear->data;
        rear = rear->prev;
        free(rear->next);
        printf("%d %u\n", data, len);
    }
}


void enqueue(queue_t **queue, int data) {
    if(*queue == NULL)
        *queue = init(data, NULL, NULL);
    *queue = init(data, *queue, NULL);
}


int main(int argc, char **argv) {
    int loops, arg;
    char op;
    queue_t *queue = NULL;
    scanf("%d", &loops);

    for(int x=1; x<= loops; ++x) {
        scanf("%c", &op);

        if(op == 'E') {
            scanf("%d", &arg);
            enqueue(&queue, arg);
        }

        else
            dequeue();
    }
    
    return 0;
}
