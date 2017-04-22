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
