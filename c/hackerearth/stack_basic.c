#include <stdio.h>

int packets = -1;

void add(int *packets_stack, int cost) {
    packets_stack[++packets] = cost;
}


void rm(int *packets_stack) {
    if(packets == -1)
        printf("No Food\n");
    else
        printf("%d\n", packets_stack[packets--]);
}

int main() {
    int tests,c,q;
    scanf("%d", &tests);
    int cost[tests];

    for(int test=0; test<tests; ++test){
        scanf("%d", &q);
        if(q == 1)
            rm(cost);
        else {
            scanf("%d", &c);
            add(cost, c);
        }
    }
    return 0;
}
