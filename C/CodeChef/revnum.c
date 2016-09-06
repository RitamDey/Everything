#include<stdio.h>
int main(){
  int t;
  scanf("%i",&t);
  for(int a=1,n;a<=t&&scanf("%i",&n);a++){
    while(n){
      int x=n%10;
      n/=10;
      printf("%i",x);
    }
    printf("\n");
  }
  return 0;
}
