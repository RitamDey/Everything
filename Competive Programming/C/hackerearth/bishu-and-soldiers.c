#include <stdio.h>


int search(int *arr, int low, int high, int key) {
    if(low > high)
        return -1;

    int mid = (low+high)/2;

    if(arr[mid] == key)
        return mid;
    else if(key < arr[mid])
        return search(arr, low, mid-1, key);
    else
        return search(arr, mid+1, high, key);
}


int sum(int *arr, int n) {
    int sum = 0;

    for(int i=0; i<n; ++i)
        sum += arr[i];

    return sum;
}


int main() {
    int len;
    scanf("%d", &len);
    int arr[len];
    for(int i=0; i<len; ++i)
        scanf("%d", &arr[i]);

    int cases;
    scanf("%d", &cases);

    while(cases--) {
        int pow;
        scanf("%d", &pow);

        if(pow >= arr[len-1]) {
            printf("%d %d\n", len, sum(arr, len));
            continue;
        }

        int pos = search(arr, 0, len-1, pow)+1;
        printf("%d %d\n", pos, sum(arr, pos));
    }

    return 0;
}
