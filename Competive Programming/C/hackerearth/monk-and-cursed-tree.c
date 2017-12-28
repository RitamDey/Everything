#include <stdio.h>
#include <malloc.h>


typedef struct _tree {
    unsigned long long int data;
    struct _tree *right;
    struct _tree *left;
} tree;


void append(tree **t, unsigned long long int data) {
    if(*t == NULL) {
        *t = (tree *)malloc(sizeof(tree));
        (*t)->data = data;
        (*t)->left = NULL;
        (*t)->right = NULL;
    }
    
    else {
        if(data > (*t)->data)
            append(&(*t)->left, data);
        else
            append(&(*t)->right, data);
    }
}


unsigned long long int subtree(tree *bst, int low) {
    if((bst->data == low)) {
        return bst->data;
    }
    
    unsigned long long int tmp = bst->data, x;

    if(low < bst->data)
        x = subtree(bst->right, low);
    else
        x = subtree(bst->left, low);
    
    tmp = (x >= tmp)?x:tmp;

    return tmp;
}


int main() {
    tree *bst = NULL;
    int len, tmp, low, high;
    scanf("%d", &len);

    for(int i=1; i<=len; ++i) {
        scanf("%d", &tmp);
        append(&bst, tmp);
    }

    scanf("%d %d", &low, &high);

    long long int left = subtree(bst, low);
    long long int right = subtree(bst, high);

    if((left > right) && (left > bst->data))
        printf("%lld\n", left);
    else if((right > left) && (right > bst->data))
        printf("%lld\n", right);
    else
        printf("%lld\n", bst->data);
    return 0;
}
