from city import City
from hospital import Hospital
from selection import Selector
import random_initializer

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
    h1 = Hospital(23, 34, 3, city)
    h2 = Hospital(16, 34, 2, city)
    h3 = Hospital(1, 1, 10, city)
    h4 = Hospital(50, 34, 2, city)
    h5 = Hospital(40, 90, 1, city)
    h6 = Hospital(3, 3, 5, city)
    h7 = Hospital(20, 80, 3, city)


    # Geração de individuo aleatório
    # random_hospitals = random_initializer.random_hospitals(5, 2, city, 2, 1)
    # for hospital in random_hospitals:
    #     print("x: " + str(hospital.x) + ", y: " + str(hospital.y) + ", range: " + str(hospital.range))

    # Geração de soluções (individuos) aleatórias
    # random_population = random_initializer.random_population(10, 5, 2, city, 2, 1)
    # i = 1
    # for individual in random_population:
    #     print("\nIndividual " + str(i))
    #     for hospital in individual:
    #         print("x: " + str(hospital.x) + ", y: " + str(hospital.y) + ", range: " + str(hospital.range))
    #     i = i + 1

    # Teste seleção por torneio
    # random_population = random_initializer.random_population(100, 5, 2, city, 2, 1)
    # selector = Selector(50)
    # tournamentWinners = selector.tournament(random_population, 10)

    # i = 1
    # for individual in tournamentWinners:
    #     print("\nWinner " + str(i))
    #     for hospital in individual:
    #         print("x: " + str(hospital.x) + ", y: " + str(hospital.y) + ", range: " + str(hospital.range))
    #     i = i + 1

    
