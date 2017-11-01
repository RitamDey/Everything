#include<stdio.h>

int main(int argc, char const *argv[]) {
  long unsigned int f=1;
  for(int a=1;a<=100;a++)
   f*=a;
  printf("%lu\n",f);
  /*long int s=0;
  while(f)
  {
    s+=(f%10);
    f/=10;
  }
  printf("%i\n",f);*/
  return 0;
}
