

class Banco:
    ''' Modelagem de um banco'''

    def __init__(self, nome, numero):
        self._nome = nome
        self._numero = numero
        self._clientes = []
        self._contas = []

    def __str__(self):
        return f'{self._nome.capitalize()} Nª {self._numero}'

    def abrir_conta(self, conta):
        self._contas.append(conta)

    def lista_contas(self):
        for conta in self._contas:
            print(conta.resumo())