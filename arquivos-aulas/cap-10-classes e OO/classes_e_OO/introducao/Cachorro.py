

class Cachorro:
    "Modelando um cachorro"

    def __init__(self, nome, idade, raca):
        " Inicializando meus atributos"
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def resumo(self):
        return f'Nome: {self.nome} Idade: {self.idade} Raça: {self.raca}'

    def atualizar_idade(self):
        self.idade += 1

    def andar(self):
        print(f'{self.nome} está andando...')

    def sentar(self):
        print(f'{self.nome} está sentando...')

    def correr(self):
        print(f'{self.nome} está correndo...')

    def latir(self):
        print(f'{self.nome} está latindo...')

