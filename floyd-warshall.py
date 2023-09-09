import sys

def floyd_warshall(graph):
    num_vertices = len(graph)
    vertices = list(graph.keys())
    distances = {v: {u: sys.maxsize for u in vertices} for v in vertices}

    for v in vertices:
        distances[v][v] = 0

    for v in graph:
        for neighbor, weight in graph[v].items():
            distances[v][neighbor] = weight

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distances[i][k] != sys.maxsize and distances[k][j] != sys.maxsize:
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances

graph = {
    'A': {'B': 5, 'C': 3, 'D': 2},
    'B': {'A': 6, 'C': 2, 'E': 4},
    'C': {'A': 3, 'B': 2, 'D': 1},
    'D': {'A': 2, 'C': 1, 'E': 7},
    'E': {'B': 4, 'D': 7}
}

all_shortest_paths = floyd_warshall(graph)

for v1 in all_shortest_paths:
    for v2 in all_shortest_paths[v1]:
        print(f'Caminho mais curto de {v1} para {v2}: {all_shortest_paths[v1][v2]}')
