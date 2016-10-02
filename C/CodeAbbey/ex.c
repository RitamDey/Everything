#include<stdio.h>

int main(){
   int range, sum = 0, tmp;
   scanf("%d", &range);
   for(int a=0; a<range; ++a){
      scanf("%d", &tmp);
      sum += tmp;
   }
   printf("%d\n", sum);
   return 0;
}
