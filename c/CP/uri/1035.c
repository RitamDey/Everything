#include<stdio.h>

int main()
{
 int a,b,c,d,indicator=0;
 scanf("%i %i %i %i",&a,&b,&c,&d);
 if((b>c)&&(d>a))
  indicator++;
 if((c+d)>(a+b))
  indicator++;
 if(!(a%2))
  indicator++;
 if(indicator==3)
  printf("Valores aceitos\n");
 else
  printf("Valores nao aceitos\n");
 return 0;
}
