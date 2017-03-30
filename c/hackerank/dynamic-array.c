#include <stdio.h>
#include <malloc.h>


typedef struct dynamic_arry_t {
    int *array;
    unsigned long long int len;
    unsigned int alloc_len;
} dynamic_array_t;


void append(dynamic_array_t *array){
    if(array->alloc_len%10 == 0){
        array->alloc_len += 10 
        realloc(array->array, array->alloc_len);
    }
}

int main(){
    int n, lastAns = 0, queries;
    scanf('%d %d', &n, &queries);
    dynamic_array_t *seqlist[n];

    for(int query=0; query<queries; ++query){
        
    }
}