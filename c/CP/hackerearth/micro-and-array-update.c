#include <stdio.h>


int get_min(int *arr, int len) {
    int min = 0;

    for(int i=1; i<len; ++i) {
        if(arr[i]<arr[min])
            min = i;
    }

    return min;
}


void get_min_time(int *arr, int len, int mark) {
    int diff = mark - arr[get_min(arr, len)];

    if(diff>0)
        printf("%d\n", diff);
    else
        puts("0");
}


int main() {
    int cases;
    scanf("%d", &cases);

    for(int i=1; i<=cases; ++i) {
        int len, mark;
        scanf("%d %d", &len, &mark);
        int arr[len];

        for(int pos=0; pos<len; ++pos)
            scanf("%d", &arr[pos]);

        get_min_time(arr, len, mark);
    }

    return 0;
}
