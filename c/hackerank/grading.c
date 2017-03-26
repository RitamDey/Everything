#include <stdio.h>


int fix_grade(int grade){
    if(grade<38){
        return grade;
    }

    if((grade+2)%5==0){
        return grade+2;
    }

    if((grade+1)%5==0){
        return grade+1;
    }

    return grade;
}


int main(){
    int len, num;
    scanf("%d", &len);
    int grades[len];

    for(int n=0; n<len; ++n){
        scanf("%d", &num);
        printf("%d\n", fix_grade(num));
    }
    return 0;
}