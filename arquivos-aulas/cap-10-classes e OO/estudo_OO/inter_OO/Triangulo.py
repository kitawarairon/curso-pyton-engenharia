class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.existencia_triangulo():
            print(f'O objeto {self} triangulo foi construido com sucesso!!!')
        else:
            raise ValueError('O triangulo não pode ser criado!!!')

    def existencia_triangulo(self):
        if abs(self.b - self.c) < self.a < self.b + self.c and abs(self.a - self.c) < self.b < self.a + self.c and \
                abs(self.a - self.b) < self.c < self.a + self.b:
            return True
        else:
            return False


class TrianguloEquilatero(Triangulo):
    pass
