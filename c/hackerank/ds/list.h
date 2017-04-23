#ifndef __LIST__
#define __LIST__

#include <stdio.h>
#include <malloc.h>
#define and &&
#define or ||
#define is ==


typedef struct Node {
    int data;
    struct Node *next;
} Node;


void print(Node *list);
Node *create(int *arr, int arr_len);

#endif
