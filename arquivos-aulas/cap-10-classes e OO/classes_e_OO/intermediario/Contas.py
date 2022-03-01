from datetime import datetime
import numpy as np


class Conta:
    ''' Modelagem de uma conta bancária'''

    def __init__(self, cliente: object, saldo: float = 0):
        ''' Inicializando os atributos da conta bancária'''
        self._saldo = saldo
        self._cliente = cliente
        self._numero = f'{np.random.randint(0,9)}{np.random.randint(0,9)}{np.random.randint(0,9)}' \
                       f'{np.random.randint(0,9)}{np.random.randint(0,9)}'
        self._operacoes = []

    @staticmethod
    def retornar_hora():
        return datetime.now()

    @property
    def saldo(self):
        return self._saldo

    @property
    def cliente(self):
        return self._cliente

    @property
    def numero(self):
        return self._numero

    @property
    def operacoes(self):
        return self._operacoes

    '''
    Movimentações bancárias
    '''

    def resumo(self):
        ''' Imprime um resumo da conta bancária'''
        return f'CC Número: {self._numero} Saldo: {self._saldo}\n' \
               f'Cliente: {self._cliente.nome} Telefone: {self._cliente.telefone}'

    def _verifica_transacao(self, valor):
        ''' Um método que verifica se é possível realizar uma transação.'''
        if self._saldo >= valor:
            return True
        else:
            return False

    def saque(self, valor):
        ''' Um método que realiza o saque da conta corrente, se for possível.'''
        if self._verifica_transacao(valor):
            self._saldo -= valor
            self._operacoes.append(f'SAQUE R${valor:.2f} | {self.retornar_hora()}')
        else:
            print('Impossível de realizar esta operação!')

    def deposito(self, valor):
        ''' Deposita um valor na conta.'''
        self._saldo += valor
        self._operacoes.append(f'DEPÓSITO: R${valor:.2f} | {self.retornar_hora()}')

    def transferencia(self, valor, conta):
        ''' Realiza uma transferência, se possível.'''
        if self._verifica_transacao(valor):
            self._saldo -= valor
            conta.deposito(valor)
            conta.operacoes.append(f'TRANSFERÊNCIA: R${valor:.2f} RECEBIDA DE {self._cliente.nome} |'
                                   f' {self.retornar_hora()}')
            self._operacoes.append(f'TRANSFERÊNCIA: R${valor:.2f} PARA {conta.cliente.nome} | {self.retornar_hora()}')
        else:
            print('Não possível realizar esta operação!')

    def extrato(self):
        ''' Imprime o extrato da conta'''
        print(f'EXTRATO CC Nº{self._numero}\n')
        for operacao in self._operacoes:
            print(f'{operacao}')
        print(f'\n Saldo atual: {self._saldo}\n')


class ContaEspecial(Conta):
    ''' Modelagem de uma conta especial.'''

    def __init__(self, cliente, saldo, limite):
        super().__init__(cliente, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def mudar_limite(self, novo_limite):
        if novo_limite > 0:
            self._limite = novo_limite
        else:
            raise ValueError('Valor inválido!')

    def _verifica_transacao(self, valor):
        if self._saldo + self._limite >= valor:
            return True
        else:
            return False









