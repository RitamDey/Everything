#include<stdio.h>

int main()
{
 int amt;
 scanf("%i",&amt);
 printf("%i\n",amt);
 int notes[]={100,50,20,10,5,2,1};
 for(int a=0;a<7;a++)
 {
  printf("%i nota(s) de R$ %i,00\n",amt/notes[a],notes[a]);
  amt%=notes[a];
 }
 return 0;
}
