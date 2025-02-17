from collections import defaultdict
INT_MAX = float('Inf')

def Min_Distance(dist, visit):
    (minimum, Minimum_Vertex) = (INT_MAX, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and not visit[vertex]:
            (minimum, Minimum_Vertex) = (dist[vertex], vertex)
    return Minimum_Vertex

def Dijkstra_Algorithm(graph, Altered_Graph, source, output_file, shortest_paths):
    tot_vertices = len(graph)
    sptSet = defaultdict(lambda: False)  # Conjunto de vértices incluídos no caminho mais curto
    dist = [INT_MAX] * tot_vertices  # Inicializa todas as distâncias como infinito
    dist[source] = 0  # A distância da fonte para ela mesma é 0

    for _ in range(tot_vertices):
        curVertex = Min_Distance(dist, sptSet)  # Encontra o vértice com menor distância
        sptSet[curVertex] = True  # Marca o vértice como visitado
        for vertex in range(tot_vertices):
            if (not sptSet[vertex] and  # Se ainda não foi visitado
                Altered_Graph[curVertex][vertex] != INT_MAX and  # Se há um caminho válido
                dist[curVertex] != INT_MAX and  # Se a distância não é infinita
                dist[vertex] > (dist[curVertex] + Altered_Graph[curVertex][vertex])):  # Se encontrou um caminho menor
                dist[vertex] = dist[curVertex] + Altered_Graph[curVertex][vertex]
    
    shortest_paths.append(dist)  # Adiciona o vetor de distâncias à matriz de caminhos mais curtos