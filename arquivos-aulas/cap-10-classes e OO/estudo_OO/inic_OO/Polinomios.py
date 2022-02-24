import matplotlib.pyplot as plt
import numpy as np


class Pol1:
    ''' Modelagem de um polinômio do primeiro grau:
    y = a * x + b
    '''
    def __init__(self, a, b):
        ''' Atributos do polinômico do primeiro grau'''
        self.a = a
        self.b = b

    def impressao_polinomio(self):
        ''' Impressão da função do primeiro grau!'''
        return f'y = {self.a:.2f}x{self.b:+.2f}'

    def raiz(self):
        ''' Raiz da função do primeiro grau!'''
        root = - self.b / self.a
        return root

    def taxa_de_crescimento(self):
        if self.a == 0:
            print('Reta horizontal!')
        elif self.a > 0:
            print('Reta crescente!')
        else:
            print('Reta decrescente!')

    def fx(self, x):
        y = self.a * x + self.b
        return y

    def plot(self, a, b):
        plt.figure()
        plt.grid()
        dominio = np.linspace(a, b, 1000)
        fx = [self.fx(x) for x in dominio]
        plt.plot(dominio, fx)
        plt.show()


class Pol2:
    ''' Criação de um objeto que represente um polinômio do segundo grau!
    y = a * x ** 2 + b * x + c
    '''

    def __init__(self, a, b, c):
        ''' Definindo os atributos da equação do segundo grau.'''
        if a == 0:
            raise ValueError('O coeficiente "a" não pode ser igual a zero!')
        else:
            self.a = a
        self.b = b
        self.c = c

    def impressao_polinomio(self):
        ''' Impressão da função do segundo grau!'''
        return f'y = {self.a:.2f}x²{self.b:+.2f}x{self.c:+.2f}'

    def concavidade(self):
        if self.a > 0:
            return 'A convidade é positiva!'
        else:
            return 'A concavidade é negativa!'

    def delta(self):
        ''' Essa função calcula o discriminante'''
        delta = pow(self.b, 2) - 4 * self.a * self.c
        return delta

    def raiz(self):
        ''' Essa função retorna as raizes'''

        if self.delta() > 0:
            x1 = (-self.b + np.sqrt(self.delta())) / 2 * self.a
            x2 = (-self.b - np.sqrt(self.delta())) / 2 * self.a
            return x1, x2

        elif self.delta() == 0:
            x0 = (-self.b + np.sqrt(self.delta())) / 2 * self.a
            return x0

        else:
            x1 = (-self.b + np.sqrt(self.delta())) / 2 * self.a
            x2 = (-self.b - np.sqrt(self.delta())) / 2 * self.a
            return x1, x2

    def fx(self, x):
        y = self.a * pow(x, 2) + self.b * x + self.c
        return y

    def plot(self, a, b):
        plt.figure()
        plt.grid()
        dominio = np.linspace(a, b, 1000)
        fx = [self.fx(x) for x in dominio]
        plt.plot(dominio, fx, color='red', ls='--')
        plt.show()












