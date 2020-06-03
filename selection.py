class Selector():
    def __init__(self, rate):
        self.selection_rate = rate

    def select_population(self, population):
        '''

        :param population: Dado uma certa população, deverá executar algum algoritmo de seleção;
        :return: A função deverá retornar os indivíduos selecionados.
        '''
        pass


    def tournament(self, sub_population):
        '''

        :param sub_population: dada uma sub-população aplicaremos a fitness function em cada indivíduo;
        :return: retornamos o mais apto dentre os indivíduos do subconjunto;
        '''
        pass

    def fitness_function(self, individual):
        '''
        Avalia cada indivíduo segundo certa função, o quão apto cada um é;
        :param individual: indivíduo a ser avaliado;
        :return: retorna o valor que representará a aptitude do indivíduo.
        '''

