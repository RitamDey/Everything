#include <stdio.h>

struct st{
  int item[10],top;
};

typedef struct st stack;

void push(stack *p){
  int num;
  puts("Enter data to push");
  scanf("%d",&num);
  p->item[++p->top] = num;
}

void disp(stack *p){
  for(int i=0;i<=p->top;i++)
    printf("%d\n",p->item[i]);
}

int pop(stack *p){
  return p->item[p->top--];
}

int main()
{
  stack s;
  int x;
  char ch = 'y';
  s.top = -1;
  while(ch == 'y'){
    printf("1.Push\n2.Display\n3.Pop\nEnter choice: ");
    scanf("%d",&x);
    switch (x){
      case 1:
        push(&s);
        break;
      case 2:
        disp(&s);
        break;
      case 3:
        printf("Popped data is %d\n", pop(&s));
        break;
      default:
        return 1;
    }
    scanf("%c",&ch);
    printf("To continue press y...");
    scanf("%c",&ch);
  }
  return 0;
}