#include<stdio.h>

int main(){
  int limit;
  scanf("%d",&limit);
  for(int a=1,n;a<=limit;a++){
    int s=0;
    scanf("%d",&n);
    for(int b=1;b<n;b++){
       if(n%b==0)
        s+=b;
    }
    printf("%d\n",s);
  }
}
