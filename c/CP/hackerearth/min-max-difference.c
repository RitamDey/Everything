#include <stdio.h>


void bubble_sort(int *arr, int len) {
    unsigned long long int t;
    for(int i=0; i<len; ++i) {
        for(int j=0; j<len-1; ++j) {
            if(arr[j]>arr[j+1]) {
                t = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = t;
            }
        }
    }
}


int main() {
    int cases, len, m;
    scanf("%d", &cases);

    for(int i=1; i<=cases; ++i) {
        scanf("%d %d", &len, &m);
        int arr[len];

        for(int i=0; i<len; ++i)
            scanf("%d", &arr[i]);

        bubble_sort(arr, len);

        int diff = len - m;

        unsigned long long int min = 0, max = 0;

        for(int i=1; i<=diff; ++i)
            max += arr[len-i];

        for(int i=0; i<diff; ++i)
            min += arr[i];

        printf("%llu\n", max-min);
    }

    return 0;
}

