#include "list.h"


Node *create(int *arr, int arr_len) {
    Node *list = (Node *)malloc(sizeof(Node));
    Node *ll = list;

    for(int pos=0; pos<arr_len; ++pos) {
        ll->data = arr[pos];
        if(pos < arr_len-1) {
            ll->next = (Node *)malloc(sizeof(Node));
            ll = ll->next;
        }
    }

    return list;
}



void print(Node *list) {
    while(list) {
        printf("%d -> ", list->data);
        list = list->next;
    }
    printf("NULL\n");
}


void append(Node *list, int data) {
    while(list->next)
        list = list->next;
    list->next = (Node *)malloc(sizeof(Node));
    list->next->data = data;
    list->next->next = NULL;
}


bool has_cycle(Node *list) {
    Node *addr[100];
    int top = -1;

    while(list) {
        for(int i=0; i<top; ++i) {
            if(addr[i] == list)
                return true;
        }
        addr[++top] = list;
        list = list->next;
    }

    return false;
}
