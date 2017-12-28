#include <stdio.h>


int main() {
    int len, n_queries;
    scanf("%d %d", &len, &n_queries);
    int arr[len];

    for(int i=0; i<len; ++i)
        scanf("%d", &arr[i]);

    for(int j=1; j<=n_queries; ++j) {
        int type;
        scanf("%d", &type);

        if(type == 0) {
            int lower, upper;
            scanf("%d %d", &lower, &upper);
            if(arr[upper-1] == 1)
                puts("ODD");
            else
                puts("EVEN");
        }
        else {
            int pos;
            scanf("%d", &pos);

            arr[pos-1] = !arr[pos-1];
        }
    }

    return 0;
}
