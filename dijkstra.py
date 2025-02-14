import math

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]


    def adicionar_aresta(self, u, v, peso):
        self.grafo[u - 1][v - 1] = peso
        self.grafo[v - 1][u - 1] = peso

    def mostra_matriz(self):
        print('Matriz de adjacência:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        #inicialização da lista de adjacencia. No momento, todo mundo tem custo -1 (infinito)
        #e todos vêm do vertice 0 (nao existe)
        #formato: [custo, vertice de onde veio]

        custo_vindo = [[-1, 0] for i in range(self.vertices)] 
        custo_vindo[origem - 1] = [0, origem]
        heap = MinHeap()
        heap.adicionar_no(0, origem)
        while heap.tamanho() > 0:
            distancia, vertice = heap.remover_no()
            for i in range(self.vertices):
                if self.grafo[vertice - 1][i] > 0: #<-- self.grafo = matriz de distancia
                    if custo_vindo[i][0] == -1 or custo_vindo[i][0] > distancia + self.grafo[vertice - 1][i]: 
                        custo_vindo[i] = [distancia + self.grafo[vertice - 1][i], vertice]
                        heap.adicionar_no(distancia + self.grafo[vertice - 1][i], i + 1)
        return custo_vindo




class MinHeap:

    def __init__(self):
        self.heap = []
        self.nos = 0

    def adicionar_no(self, peso, indice):
        self.heap.append([peso, indice])
        self.nos += 1
        f = self.nos

        while True:
            if f == 1:
                break
            p = f // 2

            if self.heap[p - 1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p - 1], self.heap[f - 1] = self.heap[f - 1], self.heap[p - 1]
                f = p

    def remover_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                p = f
        return x
    
    def tamanho(self):
        return self.nos
    
    def menor_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return 'Heap vazio.'


g = Grafo(5)

g.adicionar_aresta(1, 2, 1)
g.adicionar_aresta(1, 3, 2)
g.adicionar_aresta(2, 3, 1)
g.adicionar_aresta(2, 4, 3)
g.adicionar_aresta(3, 4, 1)
g.adicionar_aresta(3, 5, 1)
g.adicionar_aresta(4, 5, 2)
g.adicionar_aresta(4, 5, 3)

g.mostra_matriz()

resultado_dijkstra = g.dijkstra(2)
print('Resultado do Dijkstra:')
for custo, vindo_de in resultado_dijkstra:
    print(f"Custo: {custo} | Vindo de: {vindo_de}")