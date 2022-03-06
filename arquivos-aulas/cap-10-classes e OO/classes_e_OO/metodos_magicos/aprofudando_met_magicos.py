

class Pessoa:

    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome

        def __getattr__(name, atributo):
            if name == 'nomecompleto'
