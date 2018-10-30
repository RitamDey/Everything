#include <stdio.h>
#include <malloc.h>


typedef struct _node {
    int data;
    struct _node *next;
    struct _node *prev;
} node;


node *newNode(int data, node *next, node *prev) {
    node *new = (node *)malloc(sizeof(node));
    new->data = data;
    new->next = next;
    new->prev = prev;

    return new;
}


node *push(node *list, int data) {
    if (list == NULL) {
        node *curr = newNode(data, NULL, NULL);
        curr->next = curr;
        curr->prev = curr;

        return curr;
    }

    node *new = newNode(data, list, list->prev);
    list->prev->next = new;
    list->prev = new;

    return new;
}


int pop(node *list) {
    if (list == NULL)
        return -1;

    int data = list->prev->data;
    node *prev = list->prev;
    list->prev = prev->prev;
    free(prev);

    return data;
}


int main() {
    node *list = NULL;

    list = push(list, 14);
    list = push(list, 15);
    list = push(list, 16);

    printf("%d\n", pop(list));
    printf("%d\n", pop(list));
    printf("%d\n", pop(list));
    printf("%d\n", pop(list));

    return 0;
}
