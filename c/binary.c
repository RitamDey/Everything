#include <stdio.h>


int search(int *arr, int low, int high, int key) {
    if(low > high)
        return 0;

    int mid = (low + high)/2;
    

    if(arr[mid] == key)
        return 1;
    else if(key < arr[mid])
        return search(arr, low, mid, key);
    else
        return search(arr, mid, high, key);
}


int main() {
    int x[10], key;

    for(int i=0; i<10; ++i)
        scanf("%d", &x[i]);

    scanf("%d", &key);

    printf("%d", search(x, 0, 9, key));

    return 0;
}
