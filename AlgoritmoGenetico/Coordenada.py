import numpy

class Coordenada:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    @staticmethod
    def calcular_distancia(cidade1, cidade2):
        return numpy.sqrt(numpy.abs(cidade1.x - cidade2.x)**2 + numpy.abs(cidade1.y - cidade2.y)**2)

    @staticmethod
    def calcular_distancia_total(coords):
        dist = 0
        for primeiro, segundo in zip(coords[:-1], coords[1:]): #percorre todas as coordenadas
            dist += Coordenada.calcular_distancia(primeiro, segundo)
        dist += Coordenada.calcular_distancia(coords[0], coords[-1])
        return dist