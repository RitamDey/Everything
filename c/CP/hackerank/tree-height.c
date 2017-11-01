#include <bst.h>


int getHeight(bst_t *tree){
    int height = 0;

    if(tree->left == NULL && tree->right == NULL)
        return 1;
    
    if(tree->left)
        height += getHeight(tree->left)+1;
    
    if(tree->right)
        height += getHeight(tree->right)+1;
    
    return height;
}


void append(bst_t **tree, int data){
    if(*tree == NULL){
        *tree = (bst_t *)malloc(sizeof(bst_t));
        (*tree)->data = data;
        (*tree)->left = NULL;
        (*tree)->right = NULL;
    }

    if((*tree)->data > data){
        append(&(*tree)->right, data);
    }

    if((*tree)->data < data){
        append(&(*tree)->left, data);
    }
}

int main(){
    int arr[] = {1,2,4,5,6,7};
    bst_t *tree = NULL;

    append(&tree, 3);

    for(int i=0; i<6; ++i)
        append(&tree, arr[i]);
    
    printf("Height of the tree: %d\n", getHeight(tree)-1);
    return 0;
}