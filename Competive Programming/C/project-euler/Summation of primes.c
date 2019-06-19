#include <stdio.h>
#include <string.h>
#include <malloc.h>
#include <math.h>


char *generate_table(int limit) {
    char *prime_table = (char *) calloc(limit+1, sizeof(char));
    memset(prime_table, 1, limit*sizeof(char));

    prime_table[0] = 0;
    prime_table[1] = 0;

    for (int i=2; i <= floor(sqrt((double) limit)); ++i) {
        if (prime_table[i] == 1) {
            for (int j=i*i, k=1; j <= limit; j = (i*i) + k*i, k++)
                prime_table[j] = 0;
        }
    }

    return prime_table;
}


int main() {
    unsigned long int sum = 0;
    char *table = generate_table(2000000);

    for (int i=0; i <= 2000000; i++) {
        if (table[i] == 1)
            sum += i;
    }

    printf("Result is %lu\n", sum);
    return 0;
}
