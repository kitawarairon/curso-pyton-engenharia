

class Cliente:
    ''' Modelagem de um cliente.'''

    def __init__(self, nome, telefone, cpf):
        self._nome = nome.capitalize()
        if len(telefone) == 8:
            self._telefone = telefone
        else:
            raise ValueError('Número do telefone inválido!')
        if len(cpf) == 11:
            self._cpf = cpf
        else:
            raise ValueError('Número do cpf inválido!')

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if len(novo_telefone) == 8:
            self._telefone = novo_telefone

    @property
    def cpf(self):
        return self._cpf




