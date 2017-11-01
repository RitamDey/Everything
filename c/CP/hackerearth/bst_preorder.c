#include <stdio.h>
#include <stdbool.h>
#include <malloc.h>


typedef struct bst_t {
    long long int data;
    struct bst_t *right;
    struct bst_t *left;
} bst_t;


void append(bst_t **tree, long long int data) {
    if(*tree == NULL) {
        *tree = (bst_t *)malloc(sizeof(bst_t));
        (*tree)->data = data;
        (*tree)->right = NULL;
        (*tree)->left = NULL;
        return;
    }

    if((*tree)->data >= data)
        append(&(*tree)->left, data);
    else
        append(&(*tree)->right, data);
}


void pre_order(bst_t *tree) {
    /**
     * Pre-Order traversal starts by printing the root's data
     * Then the left subtree's data and descends down to left
     * Then the right subtree's data and desends down to right
    **/
    if(tree) {
        printf("%lld\n", tree->data);
        pre_order(tree->left);
        pre_order(tree->right);
    }
}


void find_subtree(bst_t *tree, long long int data) {
    if(data == 0 || data == tree->data) {
        pre_order(tree);
        return;
    }
    if(tree->data >= data)
        find_subtree(tree->left, data);
    else
        find_subtree(tree->right, data);
}


int main() {
    long long int n, d;
    bst_t *tree = NULL;
    scanf("%lld", &n);

    while(n--) {
        scanf("%lld", &d);
        append(&tree, d);
    }

    scanf("%lld", &n);
    find_subtree(tree, n);

    return 0;
}
