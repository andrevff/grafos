import sys

def calculate_bellman_ford(graph, origin):
    distances = { v: sys.maxsize for v in graph }
    distances[origin] = 0

    for _ in range(len(graph) - 1):
        for v in graph:
            for neighbor, weight in graph[v].items():
                if distances[v] + weight < distances[neighbor]:
                    distances[neighbor] = distances[v] + weight

    # Verificanndo ciclos negativos
    for v in graph:
        for neighbor, weight in graph[v].items():
            if distances[v] + weight < distances[neighbor]:
                raise ValueError("O grafo contém um ciclo negativo")

    return distances

graph = {
    'A': {'B': 5, 'C': 3, 'D': 2},
    'B': {'A': 6, 'C': 2, 'E': 4},
    'C': {'A': 3, 'B': 2, 'D': 1},
    'D': {'A': 2, 'C': 1, 'E': 7},
    'E': {'B': 4, 'D': -7}  # Mantendo uma aresta com peso negativo
}

origin = 'A'

try:
    shortest_path = calculate_bellman_ford(graph, origin)

    for destiny, distance in shortest_path.items():
        print(f'Caminho mais curto de {origin} para {destiny}: {distance}')

except ValueError as e:
    print(e)
