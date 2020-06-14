from city import City
from hospital import Hospital
from selection import Selector
import random_initializer
import solver
import cProfile
import pstats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    '''
    Esse arquivo deve ser o principal de nosso algoritmo. Um orquestrador para a realização dos processos durante a iteração.
    Processos:
        - Geração da população inicial
        - Teste do critério de parada
            - Caso nossos hospitais estejam cobrindo uma região aceitável / atendendo o número de pessoas suficiente -> Parar a execução -> emitir a resposta obtida
            - Caso o critério ainda não seja satisfeito -> segue a execução
        - Seleção para a reprodução
        - Reprodução sexuada / assexuada (crossover / clone)
        - Seleção para mutação
        - Mutação
        - Nova geração
        - Repete o procedimento
    '''
    city = City(100, 100)

    populationSize = 100
    meanNumHospital = 8
    meanHospitalRange = 3
    maxIterations = 500
    convergenceCriteria = 100
    crossOverRatio = 0.1
    mutationRatio = .9
    bestIndividual, resultDict = solver.solver1(city, populationSize=populationSize, 
    meanHospitalRange=meanHospitalRange, meanNumHospitals=meanNumHospital, maxIterations=maxIterations, convergenceCriteria=convergenceCriteria, 
    crossoverRatio=crossOverRatio, mutationRatio=mutationRatio)

    iterations = []
    worst = []
    mean = []
    best = []
    for k, v in resultDict.items():
        iterations.append(k)
        worst.append(v['Worst'])
        mean.append(v['Mean'])
        best.append(v['Best'])

    plt.plot(iterations, worst, label='Worst')
    plt.plot(iterations, mean, label='Mean')
    plt.plot(iterations, best, label='Best')
    plt.xlabel('Iterations')
    plt.ylabel('Fitness')
    plt.title('tournament - Population: '+str(populationSize)+
    ', crossover: '+str(crossOverRatio)+', mutation: '+str(mutationRatio)+
    ', iterations: '+str(maxIterations)+', convergence: '+str(convergenceCriteria))
    plt.legend()
    plt.show()