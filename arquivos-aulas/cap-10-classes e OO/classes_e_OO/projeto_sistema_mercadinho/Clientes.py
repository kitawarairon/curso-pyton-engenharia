

class Cliente:
    ''' Modelagem de um cliente de um mercadinho.'''

    def __init__(self, nome: str, email: str, cpf: str, telefone: str, compras: dict):
        self._nome = nome
        self._email = email
        self._cpf = cpf
        self._telefone = telefone
        self._compras = compras

    @property
    def nome(self):
        return self._nome

    @property
    def compras(self):
        return self._compras

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def cpf(self):
        return self._cpf

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

if __name__ == '__main__':
    compras = {}
    pedro = Cliente('pedro', 'wkitawarairon@gmail.com', '55533311122', '9988774455', compras=compras)


