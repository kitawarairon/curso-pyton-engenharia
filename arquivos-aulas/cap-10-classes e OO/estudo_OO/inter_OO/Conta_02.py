class Conta:
    ''' A tentativa de representação de uma conta bancária!'''

    def __init__(self, numero, titular, saldo, limite):
        ''' Inicializando os atributos de uma conta bancária'''
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def extrato(self):
        ''' Uma função que retorna o extrato da conta bancária!'''
        return f'O saldo de {self.__titular} é de {self.__saldo}'

    def depositar(self, valor):
        '''
        Um método que nos permite depositar na conta bancária
        :param valor: valor a ser depositado na conta bancária
        :return: None
        '''
        self.__saldo += valor

    def __verifica_saque(self, valor):
        '''
        Uma função para fazer a verificação se é possível a realização da operação de saque
        :param valor: Valor a ser avaliado!
        :return: Bool
        '''
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_para_sacar

    def sacar(self, valor):
        '''
        Um método que realiza o saque na conta bancária
        :param valor: O valor a ser sacado da conta
        :return: None
        '''
        if self.__verifica_saque(valor):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite de saque!!!'.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)