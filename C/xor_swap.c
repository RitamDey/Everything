#include<stdio.h>

/*
 * Wikipedia link: https://en.wikipedia.org/wiki/XOR_swap_algorithm
 * The code is copied from Wikipedia
*/

//int pointers so that there is no need to return anything
void xor_swap(int *x, int *y){
	if(x!=y){
		*x ^= *y;
		*y ^= *x;
		*x ^= *y;
	}
}

int main(){
	printf("A sample program to demonstrate the xor swap algorithm\n");
	int num1, num2;
	printf("Enter two number (Num1 and Num2) ");
	scanf("%d %d", &num1, &num2);
	xor_swap(&num1, &num2);
	printf("After the swap\nNum1: %d\nNum2: %d\n", num1, num2);
	return 0;
}
