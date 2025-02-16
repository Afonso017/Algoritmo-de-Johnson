from typing import List, Tuple

# Função Bellman-Ford fornecida por você
def bellman_ford(edges: List[Tuple[int, int, int]], src: int, V: int) -> List[int]:
    inf = float('inf')
    if not edges:
        return []

    dist = [inf] * V
    dist[src] = 0

    # Relaxamento das arestas
    for _ in range(V - 1):
        updated = False
        for u, v, weight in edges:
            if dist[u] != inf and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                updated = True
        if not updated:
            break

    # Verifica se tem ciclo negativo
    for u, v, weight in edges:
        if dist[u] != inf and dist[u] + weight < dist[v]:
            return [-1]

    return dist