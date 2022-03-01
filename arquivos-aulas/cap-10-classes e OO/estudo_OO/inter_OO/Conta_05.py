import numpy as np


class Conta:
    ''' A tentativa de representação de uma conta bancária!'''

    def __init__(self,  titular, saldo, limite):
        ''' Inicializando os atributos de uma conta bancária'''
        self.__numero = int(f'{np.random.randint(0,9)}{np.random.randint(0,9)}{np.random.randint(0,9)}{np.random.randint(0,9)}{np.random.randint(0,9)}')
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def __str__(self):
        return f'{self.__titular.capitalize()} | {self.__numero}'

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    ''' Operações disponíveis. '''

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
