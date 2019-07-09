#include <stdio.h>
#include <math.h>


float area(float n) {
    return cos(n);
}


int main() {
    float lower_limit, upper_limit, h, sum_even=0, sum_odd=0;
    int n;

    printf("Enter lower and upper limit: ");
    scanf("%f %f", &lower_limit, &upper_limit);

    float sum_const = area(lower_limit) + area(upper_limit);

    printf("Enter intervals: ");
    scanf("%d", &n);

    h = (upper_limit - lower_limit) / n;

    for (int i=1; i < n; i+=2)
        sum_odd += area(lower_limit + i*h);

    for (int i=2; i < n-1; i+=2)
        sum_even += area(lower_limit + i*h);

    float sum = (h/3) * (sum_const + 4*sum_odd + 2*sum_even);

    printf("Integrated value: %8.4f\n", sum);

    return 0;
}
