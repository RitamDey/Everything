#include<stdio.h>

int main(){
  int n,s;
  scanf("%d",&n);
  for(int a=1;a<=n&&scanf("%d",&s);a++){
    if(s%2==0)
     printf("%i %i\n",s/2,s/2);
    else
     printf("%i %i\n",s/2,s/2+1);
  }
  return 0;
}
