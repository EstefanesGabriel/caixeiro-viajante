import numpy
import random
from Coordenada import Coordenada

class AlgoritmoGenetico():
    def __init__(self):
        pass

    def create_population(self, size, coords):
        population = []
        for _ in range(size):
            start = coords[0]
            route = coords[1:]
            route = random.sample(route, len(route))
            route.insert(0, start)
            population.append(route)
        return population

    def evaluate_population(self, population):
        fitnesses = [Coordenada.calcular_distancia_total(route) for route in population]
        return fitnesses

    def select(self, population, fitnesses, num_best):
        best_indices = numpy.argsort(fitnesses)[:num_best]
        return [population[i] for i in best_indices]

    def crossover(self, route1, route2):
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

    def mutate(self, route, mutation_rate):
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]

    def executar(self, coords, population_size = 100, generations = 500, mutation_rate = 0.01):
        population = self.create_population(population_size, coords)
        best_route = None
        best_distance = float('inf')

        for _ in range(generations):
            fitnesses = self.evaluate_population(population)
            best_gen_route = population[numpy.argmin(fitnesses)]
            best_gen_distance = min(fitnesses)

            if best_gen_distance < best_distance:
                best_route = best_gen_route
                best_distance = best_gen_distance

            new_population = self.select(population, fitnesses, population_size // 2)
            while len(new_population) < population_size:
                parent1, parent2 = random.sample(new_population, 2)
                child = self.crossover(parent1, parent2)
                self.mutate(child, mutation_rate)
                new_population.append(child)
            
                population = new_population

        return best_route, best_distance

