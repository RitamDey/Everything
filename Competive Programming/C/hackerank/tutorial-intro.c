/**
 * Fails in HackerRank
 * Either throws a Segmentation Fault or shows time out
**/ 

#include <stdio.h>


int binary_search(int *arr, int len, int value) {
    int low = 0;
    int high = len - 1;

    while(1) {
        int mid = (int)(high - low) / 2;

        if(value > arr[mid])
            low = mid;
        
        else if(value < arr[mid])
            high = mid;
        
        else
            return mid;
    }
}


int main() {
    int value, len, arr[len];
    scanf("%d", &value);
    scanf("%d", &len);

    for(int i=0; i<len; ++i)
        scanf("%d", &arr[i]);

    printf("%d\n", binary_search(arr, len, value));

    return 0;
}
