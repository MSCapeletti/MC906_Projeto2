from city import City
from hospital import Hospital

#Uma posição no grid atendida por um hospital equivale a um ponto, 
#Uma posição no grid atendida por 2 ou mais hospitais também vale um ponto
#Uma posição no grid atendida por 0 hospitais vale 0 pontos
def fitness1(hospitals, city):
    reached = []
    for hospital in hospitals:
        reached.extend(hospital.get_reach())

    return len(set(reached))