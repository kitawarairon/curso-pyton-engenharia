
class Conta:
    ''' A tentativa de representação de uma conta bancária!'''

    def __init__(self, numero, titular, saldo, limite):
        ''' Inicializando os atributos de uma conta bancária'''
        self.__numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        ''' Uma função que retorna o extrato da conta bancária!'''
        return f'O saldo de {self.titular} é de {self.saldo}'

    def depositar(self, valor):
        '''
        Um método que deposita na conta bancária
        :param valor: valor a ser depositado na conta bancária
        :return: None
        '''
        self.saldo += valor

    def sacar(self, valor):
        '''
        Um método que realiza o saque na conta bancária
        :param valor: O valor a ser sacado da conta
        :return: None
        '''
        self.saldo -= valor
