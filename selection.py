import random
import copy
import math

def memoize_fitness(f):
    memo = {}
    def helper(x):
        x_ = tuple(x)
        if x_ not in memo:            
            memo[x_] = f(x)
        return memo[x_]
    return helper

def sum_fitness(fitness, index):
    sum = 0
    sum_index = 0
    while sum_index <= index:
        sum += fitness[sum_index]
        sum_index += 1
    return sum

#Uma posição no grid atendida por um hospital equivale a um ponto, 
#Uma posição no grid atendida por 2 ou mais hospitais também vale um ponto
#Uma posição no grid atendida por 0 hospitais vale 0 pontos
@memoize_fitness
def fitness_function1(individual):
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


class Selector():
    def __init__(self, maxPopulation):
        self.maxPopulation = maxPopulation

    def select_population(self, population):
        '''

        :param population: Dado uma certa população, deverá executar algum algoritmo de seleção;
        :return: A função deverá retornar os indivíduos selecionados.
        '''
        pass


    def tournament(self, population, tournamentSize):
        resultingPopulation = []

        while len(resultingPopulation) < self.maxPopulation:
            tournament = []
            best = -math.inf
            bestInTournament = None
            while len(tournament) < tournamentSize:
                candidate = random.choice(population)
                tournament.append(candidate)
                if fitness_function1(candidate) > best:
                    best = fitness_function1(candidate)
                    bestInTournament = candidate

            resultingPopulation.append(bestInTournament)
            population.remove(bestInTournament)
        
        return resultingPopulation

    def roulette_method(self, population, tournamentSize):
        fitness = []
        resulting_population = []
        sum = 0
        for individual_c in range(len(population)):
            fitness.append(fitness_function1(population[individual_c]))
            sum += fitness[individual_c]

        while len(resulting_population) < tournamentSize:
            random_pivot = random.randrange(int(sum))

            for individual_index in range(len(population) - 1):
                #individual_sum = 0
                if sum_fitness(fitness, individual_index) >= random_pivot:
                    resulting_population.append(population[individual_index])
                    break
        return resulting_population


   

