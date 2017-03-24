#include <stdio.h>
#include <malloc.h>
#include "graph.h"

graph_t *create_vertex(void *source){
	graph_t *vertex = (graph_t *)malloc(sizeof(graph_t));
	vertex->data = malloc(sizeof(intmax_t*10));
	vertex->edges = calloc(sizeof(10, intmax_t));
	vertex->lenght = 10;
	memcpy(vertex->data, source);
	return vertex
}

void *add_edge(graph_t *vertex1, graph_t *vertex2){
	if(vertex1 == vertex2)
		vertex1->loop = vertex2;
	else{
		if(vertex1->top == vertex1->lenght){
		vertex1->length *= 10;
		vertex1->edges = (graph_t *)realloc(sizeof(graph_t), vertex1->length);
		}
	
	if(vertex2->top == vertex2->lenght){
		vertex2->lenght *= 10;
		vertex2->edge = (graph_t *)realloc(sizeof(graph_t), vertex->lenght);
		}
	
	vertex1->edges[++vertex1->top] = vertex2;
	vertex2->edges[++vertex2->top] = vertex1;
	}
}

uint_least32_t degrees(graph_t *vertex){
	return vertex->top;
}

