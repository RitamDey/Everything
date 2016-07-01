#include<stdio.h>

int main()
{
 int code;
 float cost;
 scanf("%i %f",&code,&cost);
 switch(code)
 {
  case 1:
   cost*=4.00;
   break;
  case 2:
   cost*=4.50;
   break;
  case 3:
   cost*=5.00;
   break;
  case 4:
   cost*=2.00;
   break;
  case 5:
   cost*=1.50;
   break;
  }
  printf("Total: R$ %.2f\n",cost);
  return 0;
}
 
