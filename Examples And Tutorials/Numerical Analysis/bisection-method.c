#include <stdio.h>
#include <math.h>


float func(float x) {
    return ((x * x * x) - x - 4);
}


int main() {
    float x1, x2, x0, e;
    int k=0;

    e = 0.0001;
    printf("Enter values of x1 and x2: ");
    
    do {
        scanf("%f %f", &x1, &x2);
    } while(func(x1) * func(x2) > 0);

    printf("x1 and x2 are %f %f\n", x1, x2);
    printf("Absolute value of difference :%f\n", fabs(x1 - x2));
    
    while (fabs(x2 - x1) > e) {
        k++;

        x0 = (x1 + x2) / 2;

        printf("%2d %f %f %f %f\n", k, func(x1), func(x2), x0, fabs(x2 - x1));

        if (func(x1)*func(x2) < 0)
            x2 = x0;
        else
            x1 = x0;
    }

    printf("Root = %f\n", x0);
    printf("No of iterations = %d\n", k);
    
    return 0;
}
