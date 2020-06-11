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
    randomDestructive = rand.randint(1, 3)
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
    copiaSwap = copy.deepcopy(individual)
    
    copiaSwap = editarHospitalesSwap(copiaSwap)
    
    return copiaSwap

def editarHospitalesSwap(individuo):
    tamano = len(individuo) - 1 
    aleatorioIndividuo = rand.randint(0, tamano)
    #hospital
    hospitalAleatorio = individuo[aleatorioIndividuo]
    #mirar que cambiar en el hospital x o  y 
    aleatorioXY = rand.randint(0,1)
    
    if aleatorioXY == 0:
        y1 = getattr(hospitalAleatorio,"y")
        hospital2 = compararHospitales(individuo, hospitalAleatorio, aleatorioXY) 
        y2 = getattr(hospital2,"y")
        x1 = getattr(hospitalAleatorio,"x")
        x2 = getattr(hospital2,"x")
        hospitalAleatorio.update_position(x2,y1)
        hospital2.update_position(x1,y2) 
    else : 
        x1 = getattr(hospitalAleatorio,"x")
        hospital2 = compararHospitales(individuo,hospitalAleatorio,aleatorioXY) 
        x2 = getattr(hospital2,"x")
        y1 = getattr(hospitalAleatorio,"y")
        y2 = getattr(hospital2,"y")
        hospitalAleatorio.update_position(x1,y2)
        hospital2.update_position(x2,y1)
    return individuo

def compararHospitales(individuo, aleatorioIndividuo, aleatorioXY):
    tamano2 = len(individuo) - 1
    aleatorioIndividuo2 = rand.randint(0,tamano2)
    hospitalAleatorio2 = individuo[aleatorioIndividuo2]
    if( aleatorioXY==0): 
        while(getattr(aleatorioIndividuo,"x")==getattr(hospitalAleatorio2,"x")):
         aleatorioIndividuo2 = rand.randint(0,tamano2)
    else :
        while(getattr(aleatorioIndividuo,"y")==getattr(hospitalAleatorio2,"y")):
         aleatorioIndividuo2 = rand.randint(0,tamano2)   
    return hospitalAleatorio2
