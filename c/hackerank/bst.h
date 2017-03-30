#include <stdio.h>
#include <malloc.h>


typedef struct bst_t {
    int data;
    struct bst_t *right, *left;
}bst_t;


void append(bst_t **tree, int data);
