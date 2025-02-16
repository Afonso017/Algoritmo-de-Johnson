from bellman_ford_aux import bellman_ford
from dijkstra_aux import dijkstra

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

def johnson_algorithm(graph: Graph):
    if not graph.edges:
        return {}

    vertex_to_index = {v: i for i, v in enumerate(graph.vertices)}
    index_to_vertex = {i: v for v, i in vertex_to_index.items()}
    V = len(graph.vertices)

    edges = []
    for u, v, weight in graph.edges:
        edges.append((vertex_to_index[u], vertex_to_index[v], weight))

    # Passo 1: Adicionar um novo vértice q
    q = V
    new_edges = edges.copy()
    for v in range(V):
        new_edges.append((q, v, 0))

    # Passo 2: Executar o algoritmo de Bellman-Ford
    h = bellman_ford(new_edges, q, V + 1)
    if h == [-1]:
        return "O grafo contém um ciclo de peso negativo"

    # Passo 3: Recalcular os pesos das arestas
    reweighted_edges = []
    for u, v, weight in edges:
        reweighted_edges.append((u, v, weight + h[u] - h[v]))

    # Passo 4: Executar o algoritmo de Dijkstra para cada vértice
    distances = {}
    for u in range(V):
        dist = dijkstra(reweighted_edges, u, V)
        # Passo 5: Ajustar as distâncias
        adjusted_dist = {index_to_vertex[v]: dist[v] - h[u] + h[v] for v in range(V)}
        distances[index_to_vertex[u]] = adjusted_dist

    return distances

def read_graph_from_file(filename: str) -> Graph:
    graph = Graph()
    with open(filename, 'r') as file:
        # Ler os vértices da primeira linha
        vertices = file.readline().strip().split(',')
        for vertex in vertices:
            graph.add_vertex(vertex)

        # Ler as arestas das linhas seguintes
        for line in file:
            u, v, weight = line.strip().split(',')
            graph.add_edge(u, v, int(weight))
    return graph

def write_output_to_file(filename: str, result):
    with open(filename, 'w') as file:
        for u in result:
            file.write(f"{u}: {result[u]}\n")

if __name__ == "__main__":
    # Ler o grafo do arquivo de entrada
    input_filename = "input.txt"
    graph = read_graph_from_file(input_filename)

    # Executar o algoritmo de Johnson
    result = johnson_algorithm(graph)

    # Escrever a saída no arquivo de saída
    output_filename = "output.txt"
    write_output_to_file(output_filename, result)

    print(f"Resultado escrito em {output_filename}")