#include <stdio.h>
#include <stdbool.h>
#include <malloc.h>


typedef struct node {
    long int data;
    struct node *next;
} node;


node **tail = NULL;


void append(node **list, long int data) {
        node *n = (node *)malloc(sizeof(node));
        n->data = data;
        n->next = NULL;

        *tail = n;
        tail = &(*tail)->next;
}


void delete_friend(node **list) {
    node **tmp = list, *x;
    bool deleted = false;

    while(*tmp && (*tmp)->next != NULL) {
        if((*tmp)->data < (*tmp)->next->data) {
            x = (*tmp)->next;
            free(*tmp);
            *tmp = x;
            deleted = true;
            break;
        }

        tmp = &(*tmp)->next;
    }

    if(deleted == false)
        free(*tmp);
}


int main() {
    int cases, n_friends, n_dels, tmp;
    scanf("%d", &cases);
    
    for(int x=1; x<=cases; ++x) {
        node *list = NULL;
        tail = &list;
        scanf("%d %d", &n_friends, &n_dels);
        
        for(int i=1; i<=n_friends; ++i) {
            scanf("%d", &tmp);
            append(&list, tmp);
        }
        
        for(; n_dels >= 1; n_dels--)
            delete_friend(&list);
        
        while(list) {
            printf("%ld ", list->data);
            list = list->next;
        }

        printf("\n");
    }
    
    return 0;
}
