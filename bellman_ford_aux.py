INT_MAX = float('Inf')
def BellmanFord_Algorithm(edges, graph, tot_vertices):
    dist = [INT_MAX] * (tot_vertices + 1)
    dist[tot_vertices] = 0  # Define a distância da fonte fictícia como 0
    for i in range(tot_vertices):
        edges.append([tot_vertices, i, 0])  # Adiciona arestas fictícias com peso 0
    for _ in range(tot_vertices + 1):  # Executa o algoritmo para detectar possíveis ciclos negativos
        for source, destn, weight in edges:
            if dist[source] != INT_MAX and dist[source] + weight < dist[destn]:
                dist[destn] = dist[source] + weight

    for source, destn, weight in edges:
            if dist[source] != INT_MAX and dist[source] + weight < dist[destn]:
                return [-1]
            
    return dist[:tot_vertices]  # Retorna os pesos alterados para os vértices originais