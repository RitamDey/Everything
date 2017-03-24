#include<stdio.h>

int f(int x, int y){
    if(!x){
        return y+1;
    }
    else if(x && !y){
        return f(x-1, 1);
    }
    else{
        return f(x-1, f(x, y-1));
    }
}

int main(){
    int data1, data2;
    scanf("%d %d",&data1, &data2);
    printf("%d\n", f(data1, data2)%1000);
    return 0;
}