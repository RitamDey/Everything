#include <stdio.h>
#include <stdbool.h>


bool is_prime(unsigned long long int n) {
    if(n==1)
        return false;
    if(n==2 || n==3)
        return true;
    for(int i=2; i<=n/2; ++i) {
        if(n%i == 0)
            return false;
    }
    return true;
}


int main() {
    int count = 1;
    unsigned long long int n = 0;

    while (count <= 10001) {
        ++n;
        if(is_prime(n))
            count++;
    }

    printf("%llu\n", n);
    return 0;
}
