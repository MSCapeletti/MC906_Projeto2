
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
