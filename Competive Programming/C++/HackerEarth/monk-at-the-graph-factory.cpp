#include <iostream>
using namespace std;


bool isTree(int *degreeList, int n_vertices) {
    unsigned int degree_sum = 0;
    
    for (int i=0; i < n_vertices; ++i)
        degree_sum += degreeList[i];

    int n_edges = degree_sum / 2;

    return n_edges == (n_vertices - 1);
}


int main() {
    int n_vertices;
    cin >> n_vertices;
    int *degreeList = new int[n_vertices];

    for (int i=0; i < n_vertices; ++i)
        cin >> degreeList[i];

    if (isTree(degreeList, n_vertices))
        cout << "Yes" << endl;
    else
        cout << "No" << endl;

    return 0;
}
