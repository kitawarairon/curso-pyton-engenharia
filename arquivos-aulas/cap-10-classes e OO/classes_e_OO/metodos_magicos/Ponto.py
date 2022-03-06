import numpy as np


class Ponto:
    ''' Modelagem de um ponto no plano bi-dimensional'''

    def __init__(self, x: float, y: float, nome: str):
        ''' Inicializando os atributos do ponto.'''
        self._x = x
        self._y = y
        self._nome = nome

    def distancia(self):
        return np.sqrt(self._x ** 2 + self._y ** 2)

    def __str__(self):
        return f'{self._nome.upper()}:({self._x},{self._y})'

    def __gt__(self, other):
        return self.distancia() > other.distancia()

    def __eq__(self, other):
        x, y, w, z = self._x, self._y, other.x, other.y
        return x == w and y == z

    def __ne__(self, other):
        x, y, w, z = self._x, self._y, other.x, other.y
        return x != w or y != z

    def __add__(self, other):
        x, y = self._x + other.x, self._y + other.y
        return Ponto(x, y, f'{self._nome}+{other.nome}')

    def __sub__(self, other):
        x, y = self._x - other.x, self._y - other.y
        return Ponto(x, y, f'{self._nome}-{other.nome}')

    @property
    def nome(self):
        return  self._nome

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        self._x = valor

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):
        self.y = valor

if __name__ == '__main__':
    a = Ponto(4, 4, 'a')
    b = Ponto(4, 8, 'b')
    print(a.distancia())
    print(b.distancia())
    amenosb = a - b
    print(amenosb.distancia())