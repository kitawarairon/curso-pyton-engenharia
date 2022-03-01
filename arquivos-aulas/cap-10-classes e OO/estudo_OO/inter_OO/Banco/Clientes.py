class Cliente:
    ''' Modelagem de cliente.'''

    def __init__(self, nome, telefone):
        self.__nome = nome.capitalize()
        if self.__verificar_numero(telefone):
            self.__telefone = telefone
        else:
            raise ValueError('Número incorreto de dígitos!!!')

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @staticmethod
    def __verificar_numero(telefone):
        if len(telefone) == 8:
            return True
        else:
            return False

    def atualizar_telefone(self, novo_telefone):
        if self.__verificar_numero(novo_telefone):
            self.__telefone = novo_telefone
        else:
            print('Impossível de realizar essa operação!!!')


if __name__ == '__main__':
    pedro = Cliente('pedro', '99778844')
    print(pedro.nome)
    print(pedro.telefone)
    pedro.atualizar_telefone('88887777')
    print(pedro.telefone)
