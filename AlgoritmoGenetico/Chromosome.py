import math


class Node:
    def __init__(self, id, x, y):
        self.x = float(x)
        self.y = float(y)
        self.id = int(id)

file_name = "training_dataset"
dataset = []

with open(file_name, "r") as f:
    for line in f:
        new_line = line.strip()
        new_line = new_line.split(" ")
        id, x, y = new_line[0], new_line[1], new_line[2]
        dataset.append(Node(id=id, x=x, y=y))

N = 20

def criar_matriz_distancia(coords):
    matriz = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(0, len(matriz)-1):
        for j in range(0, len(matriz[0])-1):
            matriz[coords[i].id][coords[j].id] = math.sqrt(
                pow((coords[i].x - coords[j].x), 2) +
                pow((coords[i].y - coords[j].y), 2)
            )
    return matriz

matriz = criar_matriz_distancia(dataset)


class Chromosome:
    def __init__(self,  coords):
        self.cromossomo = coords

        cromos_representacao = []
        for i in range(0, len(coords)):
            cromos_representacao.append(self.cromossomo[i].id)
        self.cromos_representacao = cromos_representacao

        distancia = 0
        for j in range(1, len(self.cromos_representacao) - 1):
            distancia += matriz[self.cromos_representacao[j] -
                                1][self.cromos_representacao[j + 1]-1]
        self.custo = distancia

        self.valor_fitness = 1 / self.custo
