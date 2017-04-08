#include <stdio.h>
#include <stdlib.h>


void routineA(int a, int b) {
    printf("%d\n", a+b);
}


int routineB(void (*routine)(int , int )) {
    int x, y;
    scanf("%d %d", &x, &y);
    routine(x, y);
    printf("%d %d\n", x, y);
    return 0;
}


int main() {
    while(1) {
        routineB(routineA);
    }
    return 0;
}
