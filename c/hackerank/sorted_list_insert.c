#include "ds/list.h"


Node *merge_list(Node *l1, Node *l2) {
    Node **ll = &l1;

    while(l2) {

    }
    return l1;
}


int main() {
    int arr1[] = {1, 3, 5, 6};
    Node *l1 = create(arr1, 4);
    int arr2[] = {2, 4, 7};
    Node *l2 = create(arr2, 3);


    Node *merged = merge_list(l1, l2);
    print(merged);
    return 0;
}
