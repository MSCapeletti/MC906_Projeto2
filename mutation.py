import random as rand
import copy
from hospital import Hospital

def flip(individual, meanReach, reachStandardDeviation):
    # individual é um array de Hospital
    cp = individual.copy()
    num_flips = rand.randint(0, min(len(cp) - 1, 3))
    for _ in range(num_flips):
        # gera um índice aleatório pra fazer o flip
        idx = rand.randint(0, len(cp) - 1)
        hospital = cp[idx]
        city = hospital.city
        
        # gera valores aleatórios pra mudar
        x = rand.randint(0, city.width)
        y = rand.randint(0, city.height)
        reach = rand.randint(meanReach-reachStandardDeviation, meanReach+reachStandardDeviation)

        flipHospital = hospital.copy()
        
        option = rand.randint(0, 2)
        if option == 0: # muda posicao
            flipHospital.update_position(x, y)
        elif option == 1: # muda alcance
            flipHospital.update_range(reach)
        else: # option == 2, muda posicao e alcance
            flipHospital.update(x, y, reach)
        
        cp[idx] = flipHospital
    return cp

def generative(individual, meanReach, reachStandardDeviation):
    '''
    Gera um novo gene no cromossomo
    :param individual: O cromossomo a ser mutado
    :return: O cromossomo mutado
    '''
    individuo_copy = individual.copy()

    randomGenerative = rand.randint(1, 3)
    city = individual[0].city

    for _ in range(randomGenerative):
        x1 = rand.randint(0, city.width-1)
        y1= rand.randint(0, city.height-1)
        range1 = rand.randint(meanReach-reachStandardDeviation, meanReach+reachStandardDeviation)
        individuo_copy.append( Hospital(x1, y1, range1, city) )
    
    return individuo_copy


def destructive(individual):
    #gerar um aleatorio pra saber quantos hospitais seram destruidos
    copiaIndividual = individual.copy()
    randomDestructive = rand.randint(1, min(3, len(copiaIndividual)))
    j = 0
    while randomDestructive > j : 
        copiaIndividual.pop(rand.randint(0, len(copiaIndividual)-1))
        j = j+1

    return copiaIndividual
      

def swap(individual):
    '''
    Troca dois genes de posição
    :param individual: O cromossomo a ser mutado
    :return: O cromossomo mutado
    '''
    copiaSwap = individual.copy()
    
    location = rand.randint(0, len(copiaSwap)-1)

    hospital = copiaSwap[location].copy()

    hospital.update_position(hospital.y, hospital.x)

    copiaSwap[location] = hospital
    
    return copiaSwap
