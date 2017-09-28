#include <stdio.h>
#include <stdbool.h>
#include <malloc.h>


typedef struct node {
    long int data;
    struct node *next;
} node;


void append(node **list, long int data) {
    if(*list)
        append(&(*list)->next, data);
    else {
        *list = (node *)malloc(sizeof(node));
        (*list)->data = data;
        (*list)->next = NULL;
    }
}


void delete_friend(node **list) {
    node **tmp = list, *x;
    bool deleted = false;

    while((*tmp)->next) {
        if((*tmp)->data < (*tmp)->next->data) {
            x = (*tmp)->next;
            free(*tmp);
            *tmp = x;
            deleted = true;
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
        scanf("%d %d", &n_friends, &n_dels);
        
        for(int i=1; i<=n_friends; ++i) {
            scanf("%d", &tmp);
            append(&list, tmp);
        }
        
        for(int i=1; i<=n_dels; ++i)
            delete_friend(&list);
        
        while(list) {
            printf("%ld ", list->data);
            list = list->next;
        }

        printf("\n");
    }
    
    return 0;
}
