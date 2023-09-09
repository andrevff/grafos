import sys  #obter o valor máximo das distâncias representável em inteiros

def calculate_dijkstra(graph, origin):
    distances = { v: sys.maxsize for v in graph }
    distances[origin] = 0

    visited = set()

    while visited != set(distances):
        current_vertice = None
        shorter_distance = sys.maxsize

        # encontrar o vértice de menor distância atual que não foi visitado
        for v in graph:
            if v not in visited and distances[v] < shorter_distance:
                current_vertice = v
                shorter_distance = distances[v]

        visited.add(current_vertice)

        # atualizar a distância dos vértices vizinhos
        for neighbor, weight in graph[current_vertice].items():
            if distances[current_vertice] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_vertice] + weight

    return distances

graph = {
    'A': {'B': 5, 'C': 3, 'D': 2},
    'B': {'A': 5, 'C': 2, 'E': 4},
    'C': {'A': 3, 'B': 2, 'D': 1},
    'D': {'A': 2, 'C': 1, 'E': 7},
    'E': {'B': 4, 'D': 7}
}

origin = 'A'

shortest_path = calculate_dijkstra(graph, origin)

for destiny, distance in shortest_path.items():
    print(f'Camingo mais curto de {origin} para {destiny}: {distance}')