//
// Created by stux
//

#ifndef LINKEDLIST_LINKED_H
#define LINKEDLIST_LINKED_H

typedef struct node{
   int data;
  struct node *next;
}node;

node *create(int);
void display(node *);
void insert(node *, int, int);
int pop(node *);
int length(node *);
void displayAddr(node *);
void del(node *, int);
int popFirst(node *);
void push(node *);
node *insertfirst(node *, int);
void pointer_sample();
void struct_sample();

#endif //LINKEDLIST_LINKED_H
