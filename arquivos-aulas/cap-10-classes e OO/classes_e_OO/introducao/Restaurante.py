

class Restaurante:

    def __init__(self, nome: str, tipo: str, cardapio: dict):
        self.nome = nome.capitalize()
        self.tipo = tipo.capitalize()
        self.pessoas_servidas = 0
        self.status = False
        if type(cardapio) is not dict:
            raise TypeError('O cardápio deve ser em formato de dicionário.')
        else:
            self.cardapio = cardapio

    def descrever_restaurante(self):
        print(f'O nome do restaurante {self.nome}. '
              f'A cozinha do resturante é {self.tipo}')

    def abrir_restaurante(self):
        self.status = True
        print('O restaurante está aberto.')

    def verifica_se_esta_aberto(self):
        if self.status:
            return True
        else:
            return False

    def fechar_restaurante(self):
        self.status = False
        print('O restaurante está fechado.')

    def atualizar_pessoas_servidas(self):
        if self.verifica_se_esta_aberto():
            self.pessoas_servidas += 1
        else:
            print('Impossível de realizar esta operação, pois o restaurante está fechado!')

    def menu(self):
        if self.verifica_se_esta_aberto():
            print('< Menu > \n')
            for item in self.cardapio:
                print(f'{item:<10}..................... {self.cardapio[item]:>5.2f} R$')
        else:
            print('Impossível de realizar esta operação, pois o restaurante está fechado!')

    def adicionar_item(self, item, valor):
        self.cardapio[item] = valor

    def retirar_item(self, item):
        if item in self.cardapio:
            del self.cardapio[item]
        else:
            print('O item não pode ser deletado, pois está indisponível!')

if __name__ == '__main__':
    cardapio_japones = {'Sushi': 1.50, 'Têmpura': 6.50, 'Temaki': 22.50}
    #cardapio_japones = [['Sushi', 1.50]]
    hashi = Restaurante('hashi', 'japonesa', cardapio_japones)
    hashi.abrir_restaurante()
    print(hashi.pessoas_servidas)
    hashi.menu()





