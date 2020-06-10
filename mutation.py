import random as rand
import copy

def flip(individual):
    # individual é um array de Hospital
    cp = copy.deepcopy(individual)
    num_flips = rand.randint(0, len(cp) - 1)
    for _ in range(num_flips):
        # gera um índice aleatório pra fazer o flip
        idx = rand.randint(0, len(cp) - 1)
        hospital = cp[idx]
        city = hospital.city
        
        # gera valores aleatórios pra mudar
        x = rand.randint(0, city.width)
        y = rand.randint(0, city.height)
        reach = rand.randint(0, min(city.width, city.height))
        
        option = rand.randint(0, 2)
        if option == 0: # muda posicao
            hospital.update_position(x, y)
        elif option == 1: # muda alcance
            hospital.update_range(reach)
        else: # option == 2, muda posicao e alcance
            hospital.update(x, y, reach)
        
        cp[idx] = hospital
    return cp
def generative(individual):
    '''
    Gera um novo gene no cromossomo
    :param individual: O cromossomo a ser mutado
    :return: O cromossomo mutado
    '''
    
    
    copiapoblacion= individual.copy()
    for i in range (len(copiapoblacion)):

       copiapoblacion[i] = editarHospitalesGenerativo(copiapoblacion[i])
    return copiapoblacion
      
def editarHospitalesGenerativo(individuo):
    # gerar um aleatório entre 0 e 3 para saber quantos hospitais serão criados
    randomGenerative = rand.randint(1,3)
    city = individuo[0].city

    #gera os datos aleatorios de os novos hospitais
    for i in  range(randomGenerative):
        x1 = rand.randint(0, city.width-1)
        y1= rand.randint(0, city.height-1)
        range1 = rand.randint(0, 3)
        individuo.append( Hospital(x1,y1,range1,city) )
    
    return individuo


def destructive(individual):
    #gerar um aleatorio pra saber quantos hospitais seram destruidos
    copiaIndividual= individual.copy()
    for i in range (len(copiaIndividual)-1):
        copiaIndividual[i] = editarHospitalesDestructivo(copiaIndividual[i])
    return copiaIndividual

def editarHospitalesDestructivo(individuoD):
    randomDestructive= rand.randint(1,len(individuoD)-1)
    j=0
    while randomDestructive > j : 
        individuoD.pop()
        j=j+1
    return individuoD   

def swap(individual):
    '''
    Troca dois genes de posição
    :param individual: O cromossomo a ser mutado
    :return: O cromossomo mutado
    '''
    copiaSwap= individual.copy()
    for i  in range (len(individual)):
        copiaSwap[i] = editarHospitalesSwap(copiaSwap[i])
    
    return copiaSwap

def editarHospitalesSwap(individuo):
    tamano = len(individuo) - 1 
    aleatorioIndividuo = rand.randint(0,tamano)
    #hospital
    hospitalAleatorio =individuo[aleatorioIndividuo]
    #mirar que cambiar en el hospital x o  y 
    aleatorioXY= rand.randint(0,1)
    atributosHospital1 = dir(hospitalAleatorio)
    
    if  aleatorioXY ==0 :
        y1 = getattr(hospitalAleatorio,"y")
        hospital2 = compararHospitales(individuo,hospitalAleatorio,aleatorioXY) 
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
    


def compararHospitales(individuo,aleatorioIndividuo,aleatorioXY):
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
