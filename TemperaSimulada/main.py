import numpy
import matplotlib.pyplot as plt
from Coordenada import Coordenada
from TemperaSimulada import TemperaSimulada

if __name__ == "__main__":
    coords = []
    for i in range(10):
        coords.append(
            Coordenada(i, numpy.random.uniform(), numpy.random.uniform()))

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
    tempera_simulada = TemperaSimulada(30, 0.99)
    coords = tempera_simulada.executar(coords)

    for primeiro, segundo in zip(coords[:-1], coords[1:]):
        ax2.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax2.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax2.plot(c.x, c.y, 'ro')

    plt.show()