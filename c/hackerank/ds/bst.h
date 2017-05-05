#ifndef BST_H
#define BST_H

#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>
#define and &&
#define or ||
#define not !
#define is ==


typedef struct bst_t {
    long long int data;
    struct bst_t *right;
    struct bst_t *left;
} bst_t;


void append(bst_t **tree, long long int data);
void pre_order(bst_t *tree);
void find_subtree(bst_t *tree, long long int data);


#endif
