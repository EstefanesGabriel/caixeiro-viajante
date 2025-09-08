from Coordenada import Coordenada
class EscolhaGulosa():
    def __init__(self):
        pass

    def executar(self, coords):
        menor = float('inf')
        for i in range(len(coords)):
            menor_index = i+1
            for j in range(i+1, len(coords)):
                if Coordenada.calcular_distancia(coords[i], coords[j]) < menor:
                    menor = Coordenada.calcular_distancia(coords[i], coords[j])
                    menor_index = j
            if i+1 != menor_index:
                coords[menor_index], coords[i+1] = coords[i+1], coords[menor_index]
            menor = float('inf')

        return coords, Coordenada.calcular_distancia_total(coords)
