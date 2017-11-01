#include <stdio.h>
#include "ds/bst.h"


void print_right(bst_t *tree) {
    printf("%d\n", tree->data);
    if(tree->right) {
        print_right(tree->right);
    }
}


void print_top(bst_t *tree) {
    if(tree->right != NULL)
        print_right(tree->right);
    
    printf("%d", tree->data);
    
    if(tree->left != NULL)
        print_top(tree->left);
}


int main() {
    bst_t *tree = NULL;
    int arr[] = {3, 5, 2, 6, 1, 7};
    for(int i=0; i<6; ++i)
        append(&tree, arr[i]);
    print_top(tree);
    return 0;
}
