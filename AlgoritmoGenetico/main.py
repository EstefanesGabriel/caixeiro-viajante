import numpy
import random
import matplotlib.pyplot as plt
from Coordenada import Coordenada

def create_population(size, coords):
    population = []
    for _ in range(size):
        start = coords[0]
        route = coords[1:]
        route = random.sample(route, len(route))
        route.insert(0, start)
        population.append(route)
    return population

def evaluate_population(population):
    fitnesses = [Coordenada.calcular_distancia_total(route) for route in population]
    return fitnesses

def select(population, fitnesses, num_best):
    best_indices = numpy.argsort(fitnesses)[:num_best]
    return [population[i] for i in best_indices]

def crossover(route1, route2):
    start, end = sorted(random.sample(range(len(route1)), 2))
    child = [None] * len(route1)
    child[start:end] = route1[start:end]
    pointer = 0
    for city in route2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city
    return child

def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

def genetic_algorithm(coords, population_size = 100, generations = 500, mutation_rate = 0.01):
    population = create_population(population_size, coords)
    best_route = None
    best_distance = float('inf')

    for _ in range(generations):
        fitnesses = evaluate_population(population)
        best_gen_route = population[numpy.argmin(fitnesses)]
        best_gen_distance = min(fitnesses)

        if best_gen_distance < best_distance:
            best_route = best_gen_route
            best_distance = best_gen_distance

        new_population = select(population, fitnesses, population_size // 2)
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(new_population, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        
            population = new_population

    return best_route, best_distance

if __name__ == "__main__":
    coords = []
    for i in range(10):
        coords.append(
            Coordenada(i, numpy.random.uniform(), numpy.random.uniform())
        )

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

    best_route, best_distance = genetic_algorithm(coords)

    for primeiro, segundo in zip(best_route[:-1], best_route[1:]):
        ax2.plot([primeiro.x, segundo.x], [primeiro.y, segundo.y], 'b')
    ax2.plot([best_route[0].x, best_route[-1].x], [best_route[0].y, best_route[-1].y], 'b')
    for c in best_route:
        ax2.plot(c.x, c.y, 'ro')

    plt.show()
