import matplotlib.pyplot as plt
import numpy as np


class Eq1:
    '''
    Tentativa de modelagem de uma equação do primeiro grau.
    y = a * x + b
    '''

    def __init__(self, a, b):
        ''' Atributos de uma equação do primeiro grau.'''
        self.a = a
        self.b = b

    def impressao_polinomio(self):
        ''' Impressãp de uma função do primeiro grau.'''
        return f'y={self.a:.1f}x{self.b:+.1f}'

    def zero_da_funcao(self):
        ''' Retorna o zero da função.'''
        return - self.b / self.a

    def taxa_de_crescimento(self):
        if self.a == 0:
            print('Reta horizontal.')
        elif self.a > 0:
            print('Reta crescente.')
        else:
            print('Reta decrescente.')

    def fx(self, x):
        y = self.a * x + self.b
        return y

    @staticmethod
    def verifica_dominio(inf, sup):
        if inf > sup:
            return True
        else:
            return False

    def plot(self, inf, sup):
        if self.verifica_dominio(inf, sup):
            raise ValueError('Valores inválidos: inf <= sup')
        else:
            plt.figure()
            plt.grid()
            dominio = np.linspace(inf, sup, 10000)
            fx = [self.fx(x) for x in dominio]
            plt.plot(dominio, fx, ls=':', color='navy')
            plt.show()


class Eq2:
    ''' Modelagem de uma equação do segundo grau.
    y = a * x ** 2 + b * x + c
    '''

    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError('O coeficiene "a" não pode ser igual à zero.')
        else:
            self.a = a
        self.b = b
        self.c = c

    def impressao_polinomio(self):
        return f'y={self.a:.2f}x²{self.b:+.2f}x{self.c:+.2f}'

    def concavidade(self):
        if self.a > 0:
            return 'A concavidade é positava.'
        else:
            return 'A concavidade é negativa'

    def delta(self):
        delta = pow(self.b, 2) - 4 * self.a * self.c
        return delta

    def raiz(self):
        ''' Essa função retorna as raizes'''

        if self.delta() > 0:
            x1 = (-self.b + np.sqrt(self.delta())) / 2 * self.a
            x2 = (-self.b - np.sqrt(self.delta())) / 2 * self.a
            return x1, x2

        elif self.delta == 0:
            x0 = (-self.b + np.sqrt(self.delta())) / 2 * self.a
            return x0

        else:
            return f'Raizes complexas!'

    def fx(self, x):
        y = self.a * pow(x, 2) + self.b * x + self.c
        return y

    def plot(self, inf, sup):
        plt.figure()
        plt.grid()
        dominio = np.linspace(inf, sup, 10000)
        fx = [self.fx(x) for x in dominio]
        plt.plot(dominio, fx, ls='--', color='pink')
        plt.show()




if __name__ == '__main__':
    eq2 = Eq2(1, -3, 1)
    eq2.plot(-3, 3)
