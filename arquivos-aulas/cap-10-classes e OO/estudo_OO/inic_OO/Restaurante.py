class Restaurante:
    " Essa classe representa um restaurante."

    def __init__(self, nome, tipo):
        self.nome = nome.capitalize()
        self.tipo = tipo.capitalize()
        self.pessoas_servidas = 0
        self.status = False
        self.cardapio = {'Sushi': 3.00, 'Yakisoba': 12.50,
                     'Tempura': 16.90, 'Temaki': 23.45}
        print('O restaurante foi criado, mas está fechado!')

    def descrever_restaurante(self):
        print(f'O nome do restaurante é {self.nome}. '
              f'A cozinha do restaurante é {self.tipo}')

    def ataulizar_pessoas_servidas(self):
        self.pessoas_servidas += 1

    def abrir_restaurante(self):
        self.status = True
        print('O restaurante está aberto!')

    def fechar_restaurante(self):
        self.status = False
        print('O resturante está fechado!')

    def menu(self):
        print('Menu: ')
        for item in self.cardapio:
            print(f'{item:<10} ................... {self.cardapio[item]:>5.2f} R$')

    def adicionar_item(self, item, valor):
        self.cardapio[item] = valor

    def retirar_item(self, item):
        if item in self.cardapio:
            del self.cardapio[item]
        else:
            print('O item não está disponível!')


if __name__ == '__main__':
    japa = Restaurante('HASHI', 'JAPONESA')
    print(japa.tipo)
    print(japa.status)
    print(japa.menu())
    japa.adicionar_item('Sorvete', 12.45)
    print(japa.menu())
    japa.retirar_item('Sushiasd')
    print(japa.menu())