#include<stdio.h>

int iters = 0;

void print_array(int *array, int len){
    printf("Iter %d: ", iters++);
    for(int index=0; index<len; ++index)
	printf("%d ", array[index]);
    printf("\n");
}

void bubble_sort(int *array, int l){
    int len = l;
    short done = 0;

    while(!done){
	done = 1;
	for(int i=0; i<len; ++i){
	    if(array[i] > array[i+1]){
		int tmp = array[i];
		array[i] = array[i+1];
		array[i+1] = tmp;
		done = 0;
	    }
	}
	len--;
	print_array(array, l);
    }
}

int main(){
    int number[12] = {12,11,10,9,8,7,6,5,4,3,2,1};
    int n = 12;
    print_array(number, n);
    bubble_sort(number, n);
    print_array(number, n);
    return 0;
}
