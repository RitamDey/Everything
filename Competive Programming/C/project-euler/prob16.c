#include<stdio.h>

unsigned long int r=2;

unsigned long int power(){
 int n=2;
 for(long a=1;a<=1000;a++){
  r*=n;
 }
}
int main(){
 int sum=0;
 while(r!=0){
  int x=r%10;
  sum+=x;
  r/=10;
 }
 printf("%i\n",sum);
 return 0;
}
