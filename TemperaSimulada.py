import numpy
from Coordenada import Coordenada

class TemperaSimulada:
    def __init__(self, temperatura, fator):
        self.temperatura = temperatura
        self.fator = fator

    def executar(self, coords):
        cost_list = []
        custo0 = Coordenada.calcular_distancia_total(coords)

        self.temperatura = 30
        self.fator = 0.99
        
        for _ in range(1000):
            self.temperatura = self.temperatura * self.fator
            cost_list.append(custo0)
            for _ in range(100):
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
                    if x < numpy.exp((custo0 - custo1)/self.temperatura):
                        custo0 = custo1
                    else:
                        #swap - volta o que era antigamente
                        aux = coords[r1]
                        coords[r1] = coords[r2]
                        coords[r2] = aux

        return coords, custo0, cost_list
