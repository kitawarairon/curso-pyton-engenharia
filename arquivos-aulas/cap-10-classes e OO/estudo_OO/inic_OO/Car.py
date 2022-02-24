

class Car:
    ''' A tentativa de representar um carro.'''

    def __init__(self, marca, modelo, ano):
        ''' Inicializando os atributos de um carro.'''
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = 0

    def descricao_carro(self):
        ''' Devolve um nome descrito, formatado de forma elegante'''
        formatado = f'{self.ano} | {self.marca} | {self.modelo}'
        return formatado.title()

    def ler_km(self):
        ''' Exibe uma mensagem que informa a km do carro.'''
        print(f'Essa carro tem {self.km} km rodados.')

    def update_km(self, km_rodado):
        '''
        Define o valor de leitura do km (odômetro) com o valor especificado.
        '''

        if self.km <= km_rodado:
            self.km = km_rodado
        else:
            print('Impossível de atualizar, pois vc não pode dimiuir a quantidade de km rodados!')

    def incremento_km(self, km_andado):
        ''' Soma a quantiade específicado ao valor de leitura do nosso km'''
        if km_andado >= 0:
            self.km += km_andado
        else:
            print('Valores negativos não são aceitos!')
