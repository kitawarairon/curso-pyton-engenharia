

class Carro:

    def __init__(self, marca, km, ano):
        self.marca = marca
        self.km = km
        self.ano = ano

    def __str__(self):
        return f'Marca: {self.marca} km: {self.km} ano: {self.ano}'

    def informacoes(self):
        print(f'Marca: {self.marca} km: {self.km} ano: {self.ano}')


class CarroEletrico(Carro):

    # def __init__(self, marca, km, ano, bateria):
    #     super().__init__(marca, km, ano)
    #     self.bateria = bateria
    #
    def __init__(self, marca, km, ano, bateria):
        Carro.__init__(self, marca, km, ano)
        self.bateria = bateria


if __name__ == '__main__':
    gol = Carro('gol', 125, 2014)
    tesla = CarroEletrico('tesla', 0, 2021, 354)
    # gol.informacoes()
    # tesla.informacoes()
    print(tesla)

