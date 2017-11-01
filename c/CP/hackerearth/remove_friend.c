/*
 * Created by stux on 10/10/16.
*/

// TODO: Solve the HackerEarth linked list problem
#include <malloc.h>
#include <stdint.h>

typedef struct node{
  int_fast64_t data;
  struct node *next;
}node;

node *head(node **list){
  node *tmp = *list;
  *list = (*list)->next;
  free(tmp);
  return *list;
}

node *append(node *list, int_fast64_t data){
  if(!list){
    list = (node *)malloc(sizeof(node));
    list->data = data;
    list->next = NULL;
  }
  else
    list->next = append(list->next, data);
  return list;
}

node *delFriend(node **list){
  if(*list){
    if((*list)->data < (*list)->next->data){
      node *tmp = *list;
      *list = (*list)->next;
      free(tmp);
    }
  }
}

int main(){
  node *list;
  int cases;
  scanf("%d", &cases);
  for(int a=0; a<cases; ++a){
    list = NULL;
    int friends, rmNum;
    scanf("%d %d", &friends, &rmNum);
    for(int b=0; b<friends; ++b){
      int rep;
      scanf("%d", &rep);
      list = append(list, rep);
    }
    while(list){
      printf("%li ", list->data);
      list = list->next;
    }
    printf("\n");
  }
  return 0;
}
