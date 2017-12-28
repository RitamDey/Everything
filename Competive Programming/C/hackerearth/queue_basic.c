#include <stdio.h>
#include <malloc.h>


typedef struct queue_t {
    int *array;
    unsigned long int len;  // Current queue length
    unsigned long int max_len;  // Max length to let the array grow
    unsigned long int rear;  // The index where the element is present
    unsigned long int front;  // The index where the element will be deleted
} queue_t;


void init(queue_t *queue, int max_len) {
    queue->array = (int *)calloc(max_len, sizeof(int));
    queue->max_len = max_len;
    queue->len = 0;
    queue->rear = 0;
    queue->front = 0;
}

void enqueue(queue_t *queue, int data) {
    queue->array[queue->rear++] = data;
    printf("Len %lu\n", ++queue->len);
}


void dequeue(queue_t *queue) {
    if(queue->len == 0)
        printf("-1 0\n");
    else
        printf("Dequeued %d Len %lu\n", queue->array[queue->front++], --queue->len);
}


int main(int argc, char const *argv[]) {
    char op;
    int len;
    printf("Enter max len ");
    scanf("%d", &len);
    queue_t queue;
    init(&queue, len);

    for (int i = 1; i <= len; ++i) {
        int data;
        // printf("Enter op ");
        scanf("%c", &op);

        if(op == 'E') {
            // printf("Enter the data ");
            scanf("%d", &data);
            enqueue(&queue, data);
        }

        else if(op == 'D')
            dequeue(&queue);
    }
    return 0;
}
