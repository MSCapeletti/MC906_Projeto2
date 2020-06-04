class Selector():
    def __init__(self, maxPopulation):
        self.maxPopulation = maxPopulation

    def select_population(self, population):
        '''

        :param population: Dado uma certa população, deverá executar algum algoritmo de seleção;
        :return: A função deverá retornar os indivíduos selecionados.
        '''
        pass


    def tournament(self, sub_population):
        '''

        :param sub_population: dada uma sub-população aplicaremos a fitness function em cada indivíduo;
        :return: retornamos o mais apto dentre os indivíduos do subconjunto;
        '''
        pass

    def fitness_function1(self, individual):
        #Uma posição no grid atendida por um hospital equivale a um ponto, 
        #Uma posição no grid atendida por 2 ou mais hospitais também vale um ponto
        #Uma posição no grid atendida por 0 hospitais vale 0 pontos

        #Cada hospital gera uma penalidade de 1 ponto
        #O maior alcance dos hospitais também gera uma penalidade
        #O valor da aptidão será (area - custo) / max(range)
        reached = []
        custo = len(individual)
        maxRange = 1
        for hospital in individual:
            reached.extend(hospital.get_reach())
            if hospital.range > maxRange:
                maxRange = hospital.range

        area = len(set(reached))
        fitness = float(area - custo) / maxRange
        return fitness

