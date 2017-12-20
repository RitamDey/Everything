#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>
#define is ==
#define and &&
#define or ||


typedef struct _tree {
    long long int data;
    struct _tree *left;
    struct _tree *right;
} Tree;


void append(Tree **tree, long long int data) {
    if(*tree is NULL) {
        *tree = (Tree *)malloc(sizeof(Tree));
        (*tree)->data = data;
        (*tree)->left = (*tree)->right = NULL;
    }

    else {
        if((*tree)->data < data)
            append(&(*tree)->left, data);
        else if((*tree)->data > data)
            append(&(*tree)->right, data);
    }
}


bool contains(Tree *tree, long long int data) {
    if(tree is NULL)
        return false;
    if(tree != NULL and tree->data == data)
        return true;
    else if(tree->data < data)
        return contains(tree->left, data);
    else
        return contains(tree->right, data);
}


int main() {
    int cases;
    scanf("%d",  &cases);

    for(int i=1; i<=cases; ++i) {
        int init_studs_len, rem_studs_len;
        Tree *studs = NULL;

        scanf("%d %d", &init_studs_len, &rem_studs_len);

        for(int j=1; j<=init_studs_len; ++j) {
            int x;
            scanf("%d", &x);
            append(&studs, x);
        }

        for(int j=1; j<=rem_studs_len; ++j) {
            int x;
            scanf("%d", &x);

            if(contains(studs, x))
                puts("YES");
            else {
                append(&studs, x);
                puts("NO");
            }
        }
    }
}
