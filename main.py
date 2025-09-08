import numpy
import random
import matplotlib.pyplot as plt
from  Coordenada import Coordenada
from AlgoritmoGenetico import AlgoritmoGenetico
from TemperaSimulada import TemperaSimulada

if __name__ == "__main__":
    coords = []
    for i in range(10):
        coords.append(
            Coordenada(i, numpy.random.uniform(), numpy.random.uniform())
        )

    fig = plt.figure(figsize=(15, 5))
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    # Desenha o caminho entre os pontos em sequência
    for primeiro, segundo in zip(coords[:-1], coords[1:]):
        ax1.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax1.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    # Desenha os pontos
    for c in coords:
        ax1.plot(c.x, c.y, 'ro')

    algoritmo_genetico = AlgoritmoGenetico()
    tempera_simulada = TemperaSimulada(30, 0.99)
    best_route_ag, best_distance_ag = algoritmo_genetico.executar(coords)
    best_route_ts, best_distance_ts = tempera_simulada.executar(coords)

    print(f"Custo - Algoritmo Genetico: {best_distance_ag}")
    print(f"Custo - Tempera Simulada: {best_distance_ts}")

    for primeiro, segundo in zip(best_route_ag[:-1], best_route_ag[1:]):
        ax2.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax2.plot([best_route_ag[0].x, best_route_ag[-1].x], [best_route_ag[0].y, best_route_ag[-1].y], 'b')
    for c in best_route_ag:
        ax2.plot(c.x, c.y, 'ro')
    for primeiro, segundo in zip(best_route_ts[:-1], best_route_ts[1:]):
        ax3.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax3.plot([best_route_ts[0].x, best_route_ts[-1].x], [best_route_ts[0].y, best_route_ts[-1].y], 'b')
    for c in best_route_ts:
        ax3.plot(c.x, c.y, 'ro')

    plt.tight_layout()
    plt.show()
