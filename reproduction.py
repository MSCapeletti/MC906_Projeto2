from hospital import Hospital
import copy

def crossover(parent1, parent2):
    '''
    Efetua o crossover
    :param parent1: Um dos pais
    :param parent2: Outro pai
    :return: retorna os filhos gerados pela reprodução
    '''

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