#include<stdio.h>

int main() {
  int cases;
  scanf("%d",&cases);
  for(int a=1;a<=cases;a++){
    unsigned long int num;
    scanf("%lu",&num);
    int count=0;
    while (num) {
      int x=num%10;
      if(x>0){
        if(num%x==0)
         count++;
      }
      num/=10;
    }
    printf("%i\n",count);
  }
  return 0;
}
