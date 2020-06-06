import random as rand

def flip(individual):
    '''
    Cada gene a ser mutado no cromossomo recebe um valor válido
    :param individual: O cromossomo a ser mutado
    :return: O cromossomo mutado
    '''
    # individual é um array de Hospital
    cp = individual.copy()
    num_flips = rand.randint(0, len(cp) - 1)
    for _ in range(num_flips):
        # gera um índice aleatório pra fazer o flip
        idx = rand.randint(0, len(cp) - 1)
        hospital = cp[idx].copy()
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
    pass

def destructive(individual):
    '''

    :param individual:
    :return:
    '''
    pass

def swap(individual):
    '''
    Troca dois genes de posição
    :param individual: O cromossomo a ser mutado
    :return: O cromossomo mutado
    '''
    pass