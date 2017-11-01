#include<stdio.h>

int main(){
    int questions, max_difficulty, difficulty, count, skip;
	count = skip = 0;
    scanf("%d %d", &questions, &max_difficulty);
    printf("%d %d\n", questions, max_difficulty);
    for(int i=0; i<questions && skip < 2; i++){
        scanf("%d", &difficulty);
        if(difficulty < max_difficulty)
            ++count;
        else
            ++skip;
    }
    printf("%d\n", count);
    return 0;
}
