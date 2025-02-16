from typing import List, Tuple
import heapq

def dijkstra(edges: List[Tuple[int, int, int]], src: int, V: int) -> List[int]:
    dist = [float('inf')] * V
    dist[src] = 0
    priority_queue = [(0, src)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        # Se já encontramos um caminho melhor, ignoramos
        if current_distance > dist[u]:
            continue

        # Relaxamento das arestas
        for u2, v, weight in edges:
            if u2 == u:
                distance = current_distance + weight
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(priority_queue, (distance, v))

    return dist