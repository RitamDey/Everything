#include <stdio.h>


int main(){
    int alice[3], bob[3], alice_score=0, bob_score=0;
    scanf("%d %d %d", &alice[0], &alice[1], &alice[2]);
    scanf("%d %d %d", &bob[0], &bob[1], &bob[2]);

    for(int i=0; i<3; ++i){
        if(alice[i]>bob[i])
            alice_score += 1;
        else if(alice[i]<bob[i])
            bob_score += 1;
    }

    printf("%d %d\n", alice_score, bob_score);
    return 0;
}
