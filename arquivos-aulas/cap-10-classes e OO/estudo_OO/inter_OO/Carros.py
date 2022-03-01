
class Carro:

    def __init__(self, marca,  ano, km=0):
        self.marca = marca
        self.ano = ano
        self.km = km

    def __str__(self):
        return f'{self.marca} | {self.ano}'


class CarroGasolina(Carro):

    def __init__(self, marca, ano, km=0, gasolina=0):
        Carro.__init__(self, marca, ano, km)
        self.gasolina = gasolina


class CarroEletrico(Carro):

    def __init__(self, marca, ano, km=0, bateria=0):
        super().__init__(marca, ano, km)
        self.bateria = bateria

    def verificar_bateria(self):
        print(f'A batetia está com carga de {self.bateria} kWh')

if __name__ == '__main__':
    gol = CarroGasolina('Gol', 2018, 180, 123)
    tesla = CarroEletrico('Tesla', 2021, 0, 360)
    print(gol)
    print(gol.ano)
    print(gol.gasolina)
    print(tesla)
    print(tesla.ano)
    tesla.verificar_bateria()
