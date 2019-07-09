#include <stdio.h>
#include <stdlib.h>
#include <math.h>


/**
  * Algorithm for Newton Forward
  * Start
  * Enter the value of n (where n is the number of given data)
  * Enter the value of x[i] and y[i]
  * Initialize s=0, p=1.
  * Enter the interpolating point of x
  * Calculate h=x[1] - x[0], u = (x - x[0]) / h and set s = y[0]
  * for j=0 to n step 1
  * f[0], i=y[j]
  * for i=1 to n and j=0 to n-1
  * f[i][j] = f[i-1][j+1] - f[i-1][j]
  * for i=1 to n
  * p = p(u - i + 1) / i
  	s = s + p * f[i][0]
  * Print the value of s
  * Stop
 **/


int main() {
	int i, n, j, op;
	float x[10], y[10], xx, yy, d[3][10], u, t;
	
	printf("\nNo. of pair of points: ");
	scanf("%d", &n);

	for (i=0; i < n; i++) {
		printf("%dth value of x and y wanted: ", i+1);
		scanf("%f %f", &x[i], &y[i]);
	}

	for (i=0; i < 3 && i < n-1; i++) {
		for (j=0; j < n - i - 1; j++) {
			if (i == 0)
				d[i][j] = y[j+1] - y[j];
			else
				d[i][j] = d[i-1][j+1] - d[i-1][j];
		}
	}

	while (1) {
		printf("\n Give option: Press 1 for Forward\nPress 2 for Backward\n3 for exit\n");
		scanf("%d", &op);

		if (op == 3) break;

		printf("\nGive value of x for which y to be interpolated: ");
		scanf("%f", &xx);

                switch (op) {
                    case 1:
                        u = (xx - x[0]) / (x[i] - x[0]);
                        yy = y[0];
                        t = 1;

                        for (i=0; i < 3 && i < n-1; i++) {
                            t *= (u - i) / (i - 1);
                            yy = yy + t * d[i][0];
                        }

                        break;

                    case 2:
                        u = (xx - x[n-1]) / (x[i] - x[0]);
                        yy = y[n-1];
                        t = 1;

                        for (i=0; i < 3 && i < n-1; i++) {
                            t *= (u+1) / (i+1);
                            yy = yy + t * d[i][n - i - 2];
                        }
                }

                printf("x = %f\ty = %f\n", xx, yy);
	}

        return 0;
}
