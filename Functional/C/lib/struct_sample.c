/*
 * Created by stux
*/

#include "linked.h"
#include <stdio.h>


/*
 * Created by stux
*/

//TODO: Fix the source
#include <stdio.h>
#include "linked.h"

static node list;

void creating(){
  int nodes;
  printf("Enter the total number of nodes: ");
  scanf("%d\n",&nodes);
  list = create(nodes);
}

void inserting(){
  int pos,data;
  printf("Enter the position in the &list: ");
  scanf("%d",&pos);
  printf("Enter the data to be inserted in the &list: ");
  scanf("%d",&data);
  insert(&list, pos, data);
}

void deleting(){
  int pos;
  printf("Enter the position of the element in the linked &list: ");
  scanf("%d",&pos);
  del(&list, pos);
}

int popping(){
  return pop(&list);
}

void pushing(){
  push(&list);
}

void inserting2(){
  int data;
  printf("Enter the data: ");
  scanf("%d",&data);
  &list = insertfirst(&list, data);
}

void pointer_sample(){
  puts("Performing a linked &list creation");
  creating();
  display(&list);
  puts("Performing a insertion in the &list @ a particular  position");
  inserting();
  display(&list);
  puts("Deleting a element into the &list");
  deleting();
  display(&list);
  puts("Popping a element from the last of the &list");
  printf("The popped data is: %d\n",popping());
  printf("%d %x\n",&list->data, &list->next);
  display(&list);
  puts("Inserting a last node");
  pushing();
  display(&list);
  puts("Inserting a new first node");
  inserting2();
  display(&list);
  printf("The length of the linked &list is %d\n",length(&list));
}

