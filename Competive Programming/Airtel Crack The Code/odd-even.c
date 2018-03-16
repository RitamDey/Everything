#include <stdio.h>


unsigned int check(int *arr, int i, int j)
{
    int odd = 0;
    int even = 0;

    for(; i<=j; ++i) {
        if(arr[i]%2)
            odd++;
        else
            even++;
    }

    return odd == even;
}


int main() {
    int length;
    scanf("%d", &length);
    int arr[length];

    for(int i=0; i<length; ++i)
        scanf("%d", &arr[i]);

    unsigned int subs = 0;
    for(int i=0; i<length; ++i) {
        for(int j=i; j<length; ++j) {
            //printf("%d %d %d\n", i, j, (j-i)%2 != 0);
            if((j-i)%2!=0 && check(arr, i, j))
                subs++;
        }
    }

    printf("%d\n", subs);
}
