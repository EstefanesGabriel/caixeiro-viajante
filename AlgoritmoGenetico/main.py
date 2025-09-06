import GeneticAlgorithm as GA
import Chromosome as Ch

import numpy as np
import matplotlib.pyplot as plt

numeros_geracoes = 200
tamanho_populacao = 100
velocidade_mutacao = 0.2
dataset = Ch.dataset


def algoritmo_genetico(num_geracoes, tam_populacao, vel_mutacao, data_list):
    nova_geracao = GA.inicializar(data_list, tam_populacao)

    custos_for_plot = []

    for i in range(0, num_geracoes):
        nova_geracao = GA.criar_geracao(
            nova_geracao, vel_mutacao)
        print(str(i) + ". geracao - " +
              "custo - " + str(nova_geracao[0].custo))
        custos_for_plot.append(GA.achar_melhor(nova_geracao).custo)

    return nova_geracao, custos_for_plot


def desenha_custo_geracao(y_lista):
    x_lista = np.arange(1, len(y_lista)+1)

    plt.plot(x_lista, y_lista)

    plt.title("Route custo through Generations")
    plt.xlabel("Generations")
    plt.ylabel("custo")

    plt.show()


def desenha_caminho(solucao):
    x_lista = []
    y_lista = []

    for m in range(0, len(solucao.cromossomo)):
        x_lista.append(solucao.cromossomo[m].x)
        y_lista.append(solucao.cromossomo[m].y)

    fig, ax = plt.subplots()
    plt.scatter(x_lista, y_lista)

    ax.plot(x_lista, y_lista, '--', lw=2, color='black', ms=10)
    ax.set_xlim(0, 1650)
    ax.set_ylim(0, 1300)

    plt.show()


ultima_geracao, eixo_y = algoritmo_genetico(
    num_geracoes=numeros_geracoes, tam_populacao=tamanho_populacao, vel_mutacao=velocidade_mutacao, data_list=dataset
)

melhor_solucao = GA.achar_melhor(ultima_geracao)

desenha_custo_geracao(eixo_y)

desenha_caminho(melhor_solucao)
