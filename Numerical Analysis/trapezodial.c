#include <stdio.h>
#include <stdlib.h>


float area(float n) {
    return (n*n*n) + 2;
}


int main() {
    float h, b, a, sum=0;
    int n;

    printf("Enter lower and upper bound: ");
    scanf("%f %f", &a, &b);

    float sum_const = area(a) + area(b);

    printf("Enter intervals: ");
    scanf("%d", &n);

    h = (b-a)/n;

    for (int i=1; i < n; ++i) {
        sum += (h * sum_const + 2*area(a+i*h)) / 2;
    }

    printf("Integrated value: %8.4f\n", sum);

    return 0;
}
