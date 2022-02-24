class Restaurante:
    ''' Essa classe representa uma restaurante!'''

    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        self.pessoas_servidas = 0
        self.status = False

    def descrever_restautante(self):
        print(f'O nome do restaurante é {self.nome_restaurante}')
        print(f'A cozinha do resturante é {self.tipo_cozinha}')

    def comida_servida(self):
        self.pessoas_servidas += 1

    def abrir_restaurante(self):
        self.status = True
        print('O restaurante está aberto!')

    def fechar_restaurante(self):
        self.status = False
        print('O restaurante está fechado!')

    def print_menu(self):
        print(f'''
        Bem vindo ao menu do {self.nome_restaurante}:
        - Sapo de alho: 12.00 R$
        - Temaki: 22.00 R$
        ''')



