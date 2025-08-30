import numpy
import matplotlib.pyplot as plt

class Coordenada:
    def __init__(self, x, y):
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


if __name__ == "__main__":
    coords = []
    for i in range(10):
        coords.append(
            Coordenada(numpy.random.uniform(), numpy.random.uniform()))

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    # Desenha o caminho entre os pontos em sequência
    for primeiro, segundo in zip(coords[:-1], coords[1:]):
        ax1.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax1.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    # Desenha os pontos
    for c in coords:
        ax1.plot(c.x, c.y, 'ro')

    # Têmpera Simulada
    custo0 = Coordenada.calcular_distancia_total(coords)

    t = 30
    fator = 0.99
    
    for i in range(1000):
        print(i, 'custo =', custo0)

        t = t * fator
        for j in range(100):
            r1, r2 = numpy.random.randint(0, len(coords), size=2)
            #swap
            aux = coords[r1]
            coords[r1] = coords[r2]
            coords[r2] = aux

            custo1 = Coordenada.calcular_distancia_total(coords)

            if custo1 < custo0:
                custo0 = custo1
            else:
                # Qual a chance de escolhermos um caminho pior?
                x = numpy.random.uniform()
                if x < numpy.exp((custo0 - custo1)/t):
                    custo0 = custo1
                else:
                    #swap - volta o que era antigamente
                    aux = coords[r1]
                    coords[r1] = coords[r2]
                    coords[r2] = aux

    for primeiro, segundo in zip(coords[:-1], coords[1:]):
        ax2.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax2.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax2.plot(c.x, c.y, 'ro')

    plt.show()
