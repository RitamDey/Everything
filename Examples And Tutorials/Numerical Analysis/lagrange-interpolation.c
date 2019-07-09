#include <stdio.h>
#include <math.h>


int main() {
    int i, j, n;
    float x[20], y[20], u, p, p1, sum;
    printf("Type the number of points: ");
    scanf("%d", &n);

    printf("Type the u whose value will be calculated: ");
    scanf("%f", &u);

    for (i=0; i<n; i++) {
        printf("x[%d]: ", i);
        scanf("%f", &x[i]);

        printf("y[%d]: ", i);
        scanf("%f", &y[i]);
    }

    p = 1;
    for (i=0; i<n; i++) {
        p *= (u - x[i]);
    }

    sum = 0;
    for (i=0; i<n; i++) {
        p1 = y[i] / (u - x[i]);

        for (j=0; j<n; j++) {
            if (i != j)
                p1 /= (x[i] - x[j]);
        }
    }

    sum += p1;
    p *= sum;

    for (i=0; i<n; i++)
        printf("%8.4f\t %8.4f\n", x[i], y[i]);

    printf("THe required value at u=%f is %8.4f\n", u, p);
    return 0;
}
