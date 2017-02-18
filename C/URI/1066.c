#include<stdio.h>

int main()
{
 int num,even,odd,positive,negetive;
 even=odd=positive=negetive=0;
 for(int a=1;a<=5;a++)
 {
  scanf("%i",&num);
  if(num>0)
   positive++;
  else if(num<0)
   negetive++;
  if(num%2)
   odd++;
  else
   even++;
  }
  printf("%i valor(es) par(es)\n%i valor(es) impar(es)\n%i valor(es) positivo(s)\n%i valor(es) negativo(s)\n",even,odd,positive,negetive);
  return 0;
}
