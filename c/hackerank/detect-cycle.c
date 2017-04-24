#include "ds/list.h"
#include <stdbool.h>


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


int main() {
    Node *list = (Node *)malloc(sizeof(Node));
    list->data = 1;
    list->next = NULL;

    append(list, 2);
    append(list, 3);

    // list->next->next->next = list->next;

    printf("%d\n", has_cycle(list));

    return 0;
}
