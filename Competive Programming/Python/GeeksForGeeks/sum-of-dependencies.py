def construct_graph(arr):
    pos = 0
    graph = {}
    vertex_set = set(arr)

    for vertex in vertex_set:
        graph[vertex] = 0

    while pos < len(arr) - 1:
        graph[arr[pos]] += 1
        pos += 2

    return graph


def count_dependencies(graph):
    total_sum = 0
    
    for vertex in graph:
        total_sum += graph[vertex]

    return total_sum


if __name__ == '__main__':
    for _ in range(int(input())):
        n_vertex, n_edge = map(int, input().split())
        graph = list(map(int, input().split()))
        
        print(count_dependencies(construct_graph(graph)))

