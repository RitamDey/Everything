#include <stdio.h>
#include <malloc.h>


typedef struct _node {
    int data;
    struct _node *next;
} list_t;


list_t *reverse(list_t *head) {
    list_t *prev = NULL;  // Track the previous node
    list_t *curr = head;  // Track the current node
    list_t *temp;

    // Run while we haven't completely traversed the original list
    while (curr) {
        // Store the orginal next node of the current node
        temp = curr->next;

        // Set the current node's next to point to it's previous node
        curr->next = prev;

        // Now we move to next element
        // Make the prev pointer track the current node
        prev = curr;
        // And the current node to track it's original next node
        curr = temp;
    }

    // When we are here, we have traversed the entire list and reversed it entirely
    return prev;
}


void *append(list_t **head, int data) {
    while (*head != NULL)
        head = &(*head)->next;

    *head = (list_t *) malloc(sizeof(list_t));
    (*head)->data = data;
    (*head)->next = NULL;
}


void traverse(list_t *head) {
    while (head) {
        printf("%d -> ", head->data);
        head = head->next;
    }

    printf("\n");
}


int main() {
    list_t *list = NULL;

    for (int i=1; i <= 10; ++i)
        append(&list, i);

    traverse(list);

    traverse(reverse(list));
    return 0;
}
