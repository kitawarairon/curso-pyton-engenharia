from datetime import datetime
import time
import numpy as np
from Clientes import Cliente


class Conta:
    ''' Modelando uma conta bancária.'''
    def __init__(self, clientes: object, saldo: float = 0):
        self._saldo = saldo
        self._clientes = clientes
        self._numero = f'{np.random.randint(0, 9)}{np.random.randint(0, 9)}{np.random.randint(0, 9)}{np.random.randint(0, 9)}{np.random.randint(0, 9)}'
        self._operacoes = []

    @staticmethod
    def retorna_hora():
        return datetime.now()

    @property
    def saldo(self):
        return self._saldo

    @property
    def clientes(self):
        return self._clientes

    @property
    def numero(self):
        return self._numero

    @property
    def operacoes(self):
        return self._operacoes

    def resumo(self):
        ''' Imprime um resumo da conta bancária.'''
        return f'CC Número {self._numero} Saldo: {self._saldo}\n' \
               f'Cliente: {self._clientes.nome} Telefone: {self._clientes.telefone}'

    def _verifica_transacao(self, valor):
        ''' Este método valida a retirada ou transferência.'''
        if self._saldo >= valor:
            return True
        else:
            return False

    def saque(self, valor):
        ''' Este método realiza o saque da conta, se for possível realizar a operação.'''
        if self._verifica_transacao(valor):
            self._saldo -= valor
            self._operacoes.append(f'SAQUE: R${valor:.2f} | {self.retorna_hora()}')
        else:
            print('Impossível de sacar este valor!')

    def deposito(self, valor):
        ''' Deposita um valor na conta.'''
        self._saldo += valor
        self._operacoes.append(f'DEPÓSITO: R${valor:.2f} | {self.retorna_hora()}')

    def transferencia(self, valor, conta):
        ''' Realiza uma transferência, se possível.'''
        if self._verifica_transacao(valor):
            self._saldo -= valor
            conta.deposito(valor)
            conta.operacoes.append(f'TRANSFERÊNCIA: R${valor:.2f} RECEBIDA DE {self._clientes.nome} |'
                                   f' {self.retorna_hora()}')
            self._operacoes.append(f'TRANSFERÊNCIA: R${valor:.2f} PARA {conta.clientes.nome} |'
                                    f' {self.retorna_hora()}')
        else:
            print('Não é possível realizar essa operação!')

    def extrato(self):
        ''' Imprime o extrato da conta'''
        print(f'EXTRATO CC Nº {self._numero}\n')
        for operacao in self._operacoes:
            print(f'{operacao}')
        print(f'\n Saldo atual: {self._saldo:.2f}\n')


class ContaEspecial(Conta):
    ''' Modelando uma conta especial (com limite extra)'''

    def __init__(self, clientes: object, saldo: float = 0, limite: float = 0):
        super().__init__(clientes, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, novo_limite):
        self._limite = novo_limite

    def imprime(self):
        print(self._limite, self._saldo)

    def _verifica_transacao(self, valor):
        ''' Este método valida a retirada ou transferência.'''
        if self._saldo + self._limite >= valor:
            return True
        else:
            return False


if __name__ == '__main__':
    pedro = Cliente('pedro', '99778844')
    # maria = Cliente('maria', '88779944')
    conta_pedro = Conta(pedro, 500)
    conta_pedro.saque(1000)
    # conta_maria = Conta(maria, 5000)
    # conta_pedro.deposito(150)
    # time.sleep(10)
    # conta_pedro.transferencia(500, conta_maria)
    # time.sleep(3)
    # conta_pedro.saque(600)
    # time.sleep(3)
    # conta_pedro.extrato()
    # conta_maria.extrato()
    pedro_especial = ContaEspecial(pedro, 500, 500)
    print(pedro_especial.limite)
    print(pedro_especial.saldo)
    pedro_especial.saque(1000)
    pedro_especial.extrato()
    pedro_especial.imprime()
    print(pedro_especial.retorna_hora())