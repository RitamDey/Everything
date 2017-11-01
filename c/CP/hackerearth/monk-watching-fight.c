#include "ds/bst.h"

typedef struct bst {
    bst_t;
    unsigned long long int height;
} bst;


int main() {
    bst *tree = NULL;
    long long int n, d;
    scanf("%lld", &n);

    while(n--) {
        scanf("%lld", &d);
        append(&tree, d);
    }

    pre_order(tree);

    return 0;
}
