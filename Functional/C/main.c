/*
** Created by stux
*/

#include <malloc.h>
#include <string.h>
#include "src/linked.h"

int main(){
  char *choice = (char *)malloc(sizeof(char *));
  printf("Enter the Sample you want to use:\nThe Sample Using Pointers\nThe Sample Using Normal Structure Variables\n");
  printf("Enter the name: ");
  scanf("%[^\n]s",choice);
  //if(!strcmp(choice,"The Sample Using Pointers"))
  if(!strcmp(choice,"Pointers"))
    pointer_sample();
  /*else
    struct_sample();*/
  return 0;
}
