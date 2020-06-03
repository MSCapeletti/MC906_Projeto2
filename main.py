from city import City
from hospital import Hospital

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