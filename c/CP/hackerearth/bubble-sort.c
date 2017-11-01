#include <stdio.h>


int main() {
    int len, swap;
    int n_swaps = 0;
    scanf("%d", &len);
    int arr[len];
    
    for(int i=0; i<len; ++i)
        scanf("%d", &arr[i]);

    for(int i=0; i<len; ++i) {
        for(int j=0; j<len; ++j) {
            if(arr[j] > arr[j+1]) {
                swap = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = swap;
                n_swaps++;
            }
        }
    }

    for(int i=0; i<len; ++i)
        printf("%d ", arr[i]);
    
    printf("\n%d\n", n_swaps);
    return 0;
}
