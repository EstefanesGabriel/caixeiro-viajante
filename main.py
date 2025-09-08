import numpy
import matplotlib.pyplot as plt
from  Coordenada import Coordenada
from AlgoritmoGenetico import AlgoritmoGenetico
from TemperaSimulada import TemperaSimulada
from EscolhaGulosa import EscolhaGulosa

def draw_cost_generation(y_list1, y_list2, y_list3, y_list4):
    x_list1 = numpy.arange(1, len(y_list1)+1)
    x_list2 = numpy.arange(1, len(y_list2)+1)
    x_list3 = numpy.arange(1, len(y_list3)+1)
    x_list4 = numpy.arange(1, len(y_list4)+1)

    plt.plot(x_list1, y_list1, label="Algoritmo Genético")
    plt.plot(x_list2, y_list2, label="Têmpera Simulada")
    plt.plot(x_list3, y_list3, label="Escolha Gulosa")
    plt.plot(x_list4, y_list4, label="Caminho Aleatório", linestyle='--')

    plt.title("Distância por Iteração")
    plt.xlabel("Iterações")
    plt.ylabel("Distância")
    plt.legend()

    plt.show()

def draw_final_cost(coords, best_route_guloso, best_route_ts, best_route_ag):
    fig = plt.figure(figsize=(15, 5))
    ax1 = fig.add_subplot(141)
    ax2 = fig.add_subplot(142)
    ax3 = fig.add_subplot(143)
    ax4 = fig.add_subplot(144)
    # Desenha o caminho entre os pontos em sequência
    for primeiro, segundo in zip(coords[:-1], coords[1:]):
        ax1.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax1.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    # Desenha os pontos
    for c in coords:
        ax1.plot(c.x, c.y, 'ro')
    for primeiro, segundo in zip(best_route_guloso[:-1], best_route_guloso[1:]):
        ax2.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax2.plot([best_route_guloso[0].x, best_route_guloso[-1].x], [best_route_guloso[0].y, best_route_guloso[-1].y], 'b')
    for c in best_route_guloso:
        ax2.plot(c.x, c.y, 'ro')
    for primeiro, segundo in zip(best_route_ts[:-1], best_route_ts[1:]):
        ax3.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax3.plot([best_route_ts[0].x, best_route_ts[-1].x], [best_route_ts[0].y, best_route_ts[-1].y], 'b')
    for c in best_route_ts:
        ax3.plot(c.x, c.y, 'ro')
    for primeiro, segundo in zip(best_route_ag[:-1], best_route_ag[1:]):
        ax4.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax4.plot([best_route_ag[0].x, best_route_ag[-1].x], [best_route_ag[0].y, best_route_ag[-1].y], 'b')
    for c in best_route_ag:
        ax4.plot(c.x, c.y, 'ro')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    coords = []
    for i in range(10):
        coords.append(
            Coordenada(i, numpy.random.uniform(), numpy.random.uniform())
        )



    algoritmo_genetico = AlgoritmoGenetico()
    tempera_simulada = TemperaSimulada(30, 0.99)
    escolha_gulosa = EscolhaGulosa()
    best_route_ag, best_distance_ag, cost_time_ag = algoritmo_genetico.executar(coords.copy())
    best_route_ts, best_distance_ts, cost_time_ts = tempera_simulada.executar(coords.copy())
    best_route_guloso, best_distance_guloso = escolha_gulosa.executar(coords.copy())

    print(f"Custo - Algoritmo Genetico: {best_distance_ag}")
    print(f"Custo - Tempera Simulada: {best_distance_ts}")
    print(f"Custo - Escolha Gulosa: {best_distance_guloso}")




    dist_line_guloso = []
    dist_line_aleatorio = []
    init_dist = Coordenada.calcular_distancia_total(coords)
    for _ in range(1000):
        dist_line_guloso.append(best_distance_guloso)
        dist_line_aleatorio.append(init_dist)


    draw_final_cost(coords, best_route_guloso, best_route_ts, best_route_ag)
    draw_cost_generation(cost_time_ag, cost_time_ts, dist_line_guloso, dist_line_aleatorio)
