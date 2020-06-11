import city
import random_initializer
import mutation
import reproduction
from selection import Selector, fitness_function1
import math
import random
import copy

def solver1(city, populationSize, meanNumHospitals, meanHospitalRange, 
    numHospitalsStandardDeviation=5, hospitalRangeStandardDeviation=2, 
    maxIterations=10000, convergenceCriteria=100, crossoverRatio=0.5, mutationRatio=0.5):

    print("Generating starting population..")
    generation = random_initializer.random_population(populationSize, meanNumHospitals, meanHospitalRange, city, numHospitalsStandardDeviation, hospitalRangeStandardDeviation)

    iterations = 0
    convergence = 0
    selector = Selector(populationSize)

    worst, mean, best, bestIndividual = getWorstMeanBest(generation)
    bestIndividual = copy.deepcopy(bestIndividual)

    iterationsResultDict = {}

    iterationsResultDict[iterations] = {'Best': best, 'Worst': worst, 'Mean': mean}

    while iterations < maxIterations and convergence < convergenceCriteria:

        #TODO crossover
        crossoverGeneration = []

        # mutation generated solutions
        mutatedGeneration = []
        # for each solution a random float is generated to define if a mutated child will be generated
        for solution in generation:
            mutate = random.uniform(0, 1)
            if mutate <= mutationRatio:
                # if the solution has been selected for mutation then the mutation is randomly chosen
                mutationType = random.randint(1, 3)
                if mutationType == 1:
                    mutatedGeneration.append(mutation.flip(solution, meanHospitalRange, hospitalRangeStandardDeviation))
                elif mutationType == 2:
                    mutatedGeneration.append(mutation.generative(solution, meanHospitalRange, hospitalRangeStandardDeviation))
                elif mutationType == 3:
                    mutatedGeneration.append(mutation.destructive(solution))
                else:
                    mutatedGeneration.append(mutation.swap(solution))

        generation = selector.tournament(generation + crossoverGeneration + mutatedGeneration, 10)

        iworst, imean, ibest, ibestIndividual = getWorstMeanBest(generation)

        iterationsResultDict[iterations] = {'Best': ibest, 'Worst': iworst, 'Mean': imean}

        if ibest > best:
            best = ibest
            bestIndividual = copy.deepcopy(ibestIndividual)
            convergence = 0
        
        if iterations % 10 == 0:
            print("iterations: " + str(iterations))

        iterations = iterations + 1
        convergence = convergence + 1

    return bestIndividual, iterationsResultDict


# Dada uma população qualquer retorna a fitness do melhor individuo, do pior e a média de fitness da população
def getWorstMeanBest(population):
    worst = math.inf
    mean = 0
    best = - math.inf
    bestIndividual = None

    for individual in population:
        fitness = fitness_function1(individual)

        if fitness < worst:
            worst = fitness

        if fitness > best:
            best = fitness
            bestIndividual = individual

        mean = mean + fitness

    mean = mean / len(population)

    return worst, mean, best, bestIndividual