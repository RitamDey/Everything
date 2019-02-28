#include <stdio.h>
#include <stdlib.h>
#include <math.h>


float area(float n) {
    return cos(n);
}


int main() {
    float h, b, a, sum=0, area_sum=0;
    int n;

    printf("Enter lower and upper bound: ");
    scanf("%f %f", &a, &b);

    float sum_const = area(a) + area(b);

    printf("Enter intervals: ");
    scanf("%d", &n);

    h = (b-a)/n;

    for (int i=1; i < n; ++i)
        area_sum += area(a+i*h);

    sum = (h/2) * (sum_const + 2*area_sum);
    
    printf("Integrated value: %8.4f\n", sum);

    return 0;
}
