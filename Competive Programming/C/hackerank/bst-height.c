#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>


typedef struct bst_t {
    int data;
    struct bst_t *left;
    struct bst_t *right;
} bst_t;


void append(bst_t **tree, int data) {
    if(*tree && (data > (*tree)->data))
        append(&(*tree)->right, data);
    else if(*tree && (data <= (*tree)->data))
        append(&(*tree)->left, data);
    else {
        *tree = (bst_t *)malloc(sizeof(bst_t));
        (*tree)->data = data;
        (*tree)->left = NULL;
        (*tree)->right = NULL;
    }
}


int get_height(bst_t *tree) {
    int h = 1, left = 0, right = 0;

    if(tree->left == NULL && tree->right == NULL)
        return 0;

    if(tree->left)
        left += get_height(tree->left);
    if(tree->right)
        right += get_height(tree->right);

    h += (left>right)?left:right;

    return h;
}


void display(bst_t *tree) {
    if(tree->right)
        display(tree->right);

    printf("%d->", tree->data);

    if(tree->left)
        display(tree->left);
}


int main() {
    bst_t *tree = NULL;
    int values[] = {3, 5, 2, 1, 4, 6, 7};

    for(int i=0; i<7; ++i)
        append(&tree, values[i]);

    display(tree);
    printf("\nHeight: %d\n", get_height(tree));

    return 0;
}
