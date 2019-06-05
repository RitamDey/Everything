#include <iostream>
using namespace std;


int main() {
    int n_edges, n_vertices, vertex_1, vertex_2, queries;

    cin >> n_vertices >> n_edges;
    bool *graph[n_vertices];
    for (int i=0; i < n_vertices; i++)
        graph[i] = new bool[n_vertices];

    for (int i=1; i <= n_edges; ++i) {
        cin >> vertex_1 >> vertex_2;
        graph[vertex_1-1][vertex_2-1] = true;
        graph[vertex_2-1][vertex_1-1] = true;
    }

    cin >> queries;
    while (queries--) {
        cin >> vertex_1 >> vertex_2;

        if (graph[vertex_1-1][vertex_2-1])
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
