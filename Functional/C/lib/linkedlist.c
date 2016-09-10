/*
 * Created by cody on tux
*/


#include <stdlib.h>
#include <stdio.h>
#include "linked.h"

//TODO: Push it to the GitHub repo under Functional
//TODO: Complete the API to include all the features of C++ and Java
//TODO: Add explanations for the logic of these APIs
//TODO: Optimize the code Target : Worst Complexity and Complexity of 1

node *create(int nodes) {
  node *root = NULL,*temp;
  for(int i=1; i<=nodes; i++){
    int num;
    scanf("%d",&num);
    if(root == NULL){
      root = (node *)malloc(sizeof(node));
      root->data = num;
      root->next = NULL;
      temp = root;
    }
    else{
      temp->next = (node *)malloc(sizeof(node));
      temp->next->data = num;
      temp->next->next = NULL;
      temp = temp->next;
    }
  }
  return root;
}


void display(node *list){
  for(node *k = list; k != NULL && k != 0; k = k->next)
    //TODO: Find a way to exit immediately if the argument is 0
    printf("%d->",k->data);
  puts("");
}

void displayAddr(node *root){
  node *tmp = root;
  while(tmp != NULL){
    printf("Found a node @%p\n",tmp);
    tmp = tmp->next;
  }
}

void insert(node *root, int pos, int data){
  node *temp = root;
  for(int curr=0;curr<pos-1;++curr, temp = temp->next);
  node *p = (node *)malloc(sizeof(node));
  p->next = temp->next;
  temp->next = p;
  p->data = data;
}

//TODO: Rename inserfirst function to something more appropriate
node *insertfirst(node *root, int data){
  node *tmp = (node *)malloc(sizeof(node));
  tmp->data = data;
  tmp->next = root;
  return tmp;
}

void push(node *root){
  node *tmp = root;
  for(;tmp->next != NULL; tmp = tmp->next);
  tmp->next = (node *)malloc(sizeof(node));
  printf("Enter the data: ");
  scanf("%d",&tmp->next->data);
  tmp->next->next = NULL;
}

void del(node *root, int pos) {
  node *temp = root;
  int curr = 0;
  while(curr<pos-1){
    temp = temp->next;
    curr++;
  }
  node *k = temp->next;
  temp->next = k->next;
  free(k);
}

int length(node *root){
  node *tmp = root;
  int count;
  for (count = 1;tmp->next != NULL; ++count,tmp = tmp->next);
  return count;
}

int pop(node *root){
  node* tmp = root;
  int popped;
  if(tmp->next == NULL){
    popped = tmp->data;
    free(root);
  }
  else {
    while (tmp->next->next != NULL)
      tmp = tmp->next;
    popped = tmp->next->data;
    free(tmp->next);
    tmp->next = NULL;
  }
  return popped;
}

//TODO: Fix this function
//TODO: Give a appropriate name to this function
int popFirst(node *root){
  int popped = root->data;
  return popped;
}
