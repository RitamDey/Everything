/**
 * See the selection sort method at 
 * "/media/eosHome/stux/Git/My-Simple-Programs/java/Derek Banas JavaAlgorithms/sorting1.java"
**/ 

#include <stdio.h>


void printArray(int *arr, unsigned int len) {
    for(int i=0; i<len; ++i)
        printf("%d ", arr[i]);
    printf("\n");
}


void selection_sort(int *arr, unsigned int len) {
    int minimum, temp;
    
    for(int i=0; i<len; ++i) {
        minimum = i;

        for(int y=i; y<len; ++y) {
            if(arr[minimum] > arr[y])
                minimum = y;
        }

        temp = arr[i];
        arr[i] = arr[minimum];
        arr[minimum] = temp;
    }
}


int main() {
    int array[] = {1, 5, 9, 58, 8, 18, 82, 3, 78};
    int len = 10;

    printArray(array, len);
    selection_sort(array, len);
    printArray(array, len);

    return 0;
}
