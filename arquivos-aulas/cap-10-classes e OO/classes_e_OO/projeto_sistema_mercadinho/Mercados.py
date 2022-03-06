from Clientes import Cliente


class Mercado:
    ''' Modelagem de um sistema de mercadinho'''

    def __init__(self, usuario):
        self._usuario = usuario
        self._produtos = {'arroz': [2.50, 1000], 'feijao': [4.50, 1500]}
        self._status = False
        self._extrato = []

    @property
    def usuario(self):
        return self._usuario.nome

    @property
    def produtos(self):
        return self._produtos

    @property
    def status(self):
        return self._status

    def abrir_mercadinho(self):
        ''' Método para abrir o sistema do mercadinho'''
        self._status = True

    def fechar_mercadinho(self):
        ''' Método para fechar o sistema do mercadinho'''
        self._status = False

    def _verificar_status(self):
        ''' Essa função faz a verificação do status do mercadinho'''
        if self._status:
            return True
        else:
            return False

    def adicionar_produto(self, produto: str, valor: float, quantidade: int):
        ''' Essa função adiciona um produto no "banco de dados do mercadinho". '''
        if self._verificar_status():
            self._produtos[produto.lower()] = [valor, quantidade]
        else:
            print('Operação indisponível!')

    def produtos_disponiveis(self):
        ''' Essa função imprime os produtos disponíves.'''
        if self._verificar_status():
            for produto in self._produtos:
                print(f'{produto.capitalize():<10} -------- Preço: {self._produtos[produto][0]:.2f} R$ | '
                      f'Quantidade disponível: {self._produtos[produto][1]} unidades')
        else:
            print('Operação indisponível!')

    def _conta(self):
        if self._verificar_status():
            soma = 0
            compra_cliente = self._usuario.compras
            for produto in self._produtos:
                if produto in compra_cliente:
                    extrato_produto = f'{produto.capitalize()} | {self._produtos[produto][0]}x' \
                                      f'{compra_cliente[produto]} = ' \
                                      f'{self._produtos[produto][0] * compra_cliente[produto]}'
                    self._extrato.append(extrato_produto)
                    soma += self._produtos[produto][0] * compra_cliente[produto]
                    #self._produtos[produto] -= 1
            total_conta = f'Total: {soma} R$'
            self._extrato.append(total_conta)
            return True
        else:
            print('Operação inválida!')

    def imprimir_extrato(self):
        if self._verificar_status() and self._conta():
            print()
            for item in self._extrato:
                print(item)
        else:
            print('Operação inválida!')


    def pagamento(self, tipo):
        if self._verificar_status():
            if tipo == 'debito':
                valor = input('Valor em dinheiro: ')






if __name__ == '__main__':
    compras = {'feijao': 3, 'arroz': 5}
    pedro = Cliente('pedro', 'wkitawarairon@gmail.com', '55533311122', '9988774455', compras=compras)
    print(pedro.compras)
    python_mercado = Mercado(pedro)
    python_mercado.abrir_mercadinho()
    python_mercado.imprimir_extrato()

