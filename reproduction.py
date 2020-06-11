from hospital import Hospital
import copy
import math
import random 


def crossover(parent1, parent2):
    '''
    Efetua o crossover
    :param parent1: Um dos pais
    :param parent2: Outro pai
    :return: retorna os filhos gerados pela reprodução
    '''    

    #num_to_select = random.randint(2)    #defina o número de elementos a selecionar 
    num_to_select = math.floor((len(parent2)+len(parent1))/4)

    #puxa aleatoriamente itens dos pais
    list_of_random_items_parent1 = random.sample(parent1, num_to_select) 
    list_of_random_items_parent2 = random.sample(parent2, num_to_select)

    child = [] #crie uma lista para filho 1
    child2 = [] #crie uma lista para filho 2

    #coloca os elementos aleatórios no filho 1
    child.extend(list_of_random_items_parent1)
    child.extend(list_of_random_items_parent2)

    #coloque os itens que não foram levados para o filho 1 em o filho 2
    aux=[i for i in parent1 if i not in list_of_random_items_parent1]
    aux2=[i for i in parent2 if i not in list_of_random_items_parent2]
    
    child2.extend(aux)
    child2.extend(aux2)

    i=0 

    #mostra o resultado do crossover

    for individual in child:
      print("\nChild 1" )
      for hospital in child:
          print("x: " + str(hospital.x) + ", y: " + str(hospital.y) + ", range: " + str(hospital.range))
   
    for individual in child2:
      print("\nChild 2" )
      for hospital in child2:
          print("x: " + str(hospital.x) + ", y: " + str(hospital.y) + ", range: " + str(hospital.range))



def clone(parent):
    '''
    Efetua a clonagem
    :param parent: pai, o individuo a ser clonado
    :return: o clone
    '''
    # cp = []
    # cp.extend(map(Hospital.copy, parent))
    # return cp
    return copy.deepcopy(parent)
