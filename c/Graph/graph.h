#ifndef GRAPH_H
#define GRAPH_H

typedef struct Graph{
    void *data;
    struct Graph *edges;
    uint_least32_t top, lenght;
    struct Graph *loop;
}Graph;

typedef struct Graph graph_t;

graph_t *create_vertex(void *source);
void add_edge(graph_t *vertex1, graph_t *vertex2);
uint_least32_t degree(graph_t *vertex);

#endif