#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
    printf("Enter the number of numbers " );
    int n,sum=0;
    scanf("%i\n",&n );
    int *mem = (int *)malloc(n*sizeof(int));
    for (int count=1;count<=n;count++)
        scanf("%i",(mem+count) );
    for (int i=1; i<=n; i++)
        sum += *(mem+i);
    printf("%d\n",sum);
    free(mem);
    return 0;
}
