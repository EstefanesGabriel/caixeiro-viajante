import random
import Chromosome as ch


def criar_lista_aleatoria(n_lista):
    start = n_lista[0]

    aux = n_lista[1:]
    aux = random.sample(aux, len(aux))

    aux.insert(0, start)
    aux.append(start)
    return aux


def inicializar(data, tam_populacao):
    populacao_inicial = []
    for i in range(0, tam_populacao): 
        aux = criar_lista_aleatoria(data)
        new_ch = ch.Chromosome(aux)
        populacao_inicial.append(new_ch)
    return populacao_inicial


def selecionar(populacao): 
    ticket_1, ticket_2, ticket_3, ticket_4 = random.sample(
        range(0, 99), 4) 

    candidato_1 = populacao[ticket_1]
    candidato_2 = populacao[ticket_2]
    candidato_3 = populacao[ticket_3]
    candidato_4 = populacao[ticket_4]

    if candidato_1.valor_fitness > candidato_2.valor_fitness:
        ganhador = candidato_1
    else:
        ganhador = candidato_2

    if candidato_3.valor_fitness > ganhador.valor_fitness:
        ganhador = candidato_3

    if candidato_4.valor_fitness > ganhador.valor_fitness:
        ganhador = candidato_4

    return ganhador 


def crossover(p_1, p_2):
    um_ponto = random.randint(2, 14)

    filho_1 = p_1.cromossomo[1:um_ponto]
    filho_2 = p_2.cromossomo[1:um_ponto]

    filho_1_restante = [
        item for item in p_2.cromossomo[1:-1] if item not in filho_1]
    filho_2_restante = [
        item for item in p_1.cromossomo[1:-1] if item not in filho_2]

    filho_1 += filho_1_restante
    filho_2 += filho_2_restante

    filho_1.insert(0, p_1.cromossomo[0])
    filho_1.append(p_1.cromossomo[0])

    filho_2.insert(0, p_2.cromossomo[0])
    filho_2.append(p_2.cromossomo[0])

    return filho_1, filho_2


def crossover_dois(p_1, p_2):
    ponto_1, ponto_2 = random.sample(range(1, len(p_1.cromossomo)-1), 2)
    begin = min(ponto_1, ponto_2)
    end = max(ponto_1, ponto_2)

    filho_1 = p_1.cromossomo[begin:end+1]
    filho_2 = p_2.cromossomo[begin:end+1]

    filho_1_restante = [
        item for item in p_2.cromossomo[1:-1] if item not in filho_1]
    filho_2_restante = [
        item for item in p_1.cromossomo[1:-1] if item not in filho_2]

    filho_1 += filho_1_restante
    filho_2 += filho_2_restante

    filho_1.insert(0, p_1.cromossomo[0])
    filho_1.append(p_1.cromossomo[0])

    filho_2.insert(0, p_2.cromossomo[0])
    filho_2.append(p_2.cromossomo[0])

    return filho_1, filho_2


def crossover_mix(p_1, p_2):
    ponto_1, ponto_2 = random.sample(range(1, len(p_1.cromossomo)-1), 2)
    begin = min(ponto_1, ponto_2)
    end = max(ponto_1, ponto_2)

    filho_1_1 = p_1.cromossomo[:begin]
    filho_1_2 = p_1.cromossomo[end:]
    filho_1 = filho_1_1 + filho_1_2
    filho_2 = p_2.cromossomo[begin:end+1]

    filho_1_restante = [
        item for item in p_2.cromossomo[1:-1] if item not in filho_1]
    filho_2_restante = [
        item for item in p_1.cromossomo[1:-1] if item not in filho_2]

    filho_1 = filho_1_1 + filho_1_restante + filho_1_2
    filho_2 += filho_2_restante

    filho_2.insert(0, p_2.cromossomo[0])
    filho_2.append(p_2.cromossomo[0])

    return filho_1, filho_2


def mutacao(cromossomo):
    mutacao_index_1, mutacao_index_2 = random.sample(range(1, 19), 2)
    cromossomo[mutacao_index_1], cromossomo[mutacao_index_2] = cromossomo[mutacao_index_2], cromossomo[mutacao_index_1]
    return cromossomo


def achar_melhor(geracao):
    melhor = geracao[0]
    for n in range(1, len(geracao)):
        if geracao[n].custo < melhor.custo:
            melhor = geracao[n]
    return melhor


def criar_geracao(geracao_anterior, vel_mutacao):
    nova_geracao = [achar_melhor(geracao_anterior)]

    for a in range(0, int(len(geracao_anterior)/2)):
        parent_1 = selecionar(geracao_anterior)
        parent_2 = selecionar(geracao_anterior)

        filho_1, filho_2 = crossover_mix(parent_1, parent_2)
        filho_1 = ch.Chromosome(filho_1)
        filho_2 = ch.Chromosome(filho_2)

        if random.random() < vel_mutacao:
            mutated = mutacao(filho_1.cromossomo)
            filho_1 = ch.Chromosome(mutated)

        nova_geracao.append(filho_1)
        nova_geracao.append(filho_2)

    return nova_geracao
