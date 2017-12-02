#include <stdio.h>


void convert(int n, int base) {
    if(n <= 1) {
        printf("%d", n);
        return;
    }
    convert(n/base, base);

    int rem = n%base;

    if(rem <= 9)
        printf("%d", rem);
    else
        printf("%c", rem+55);
}


int main() {
    printf("Binary of 23: ");
    convert(79, 2);
    puts("");
    convert(79, 8);
    puts("");
    convert(79, 16);
    return 0;
}
