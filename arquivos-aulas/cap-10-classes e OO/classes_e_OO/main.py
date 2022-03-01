import time
from intermediario.Clientes import Cliente
from intermediario.Contas import Conta, ContaEspecial
from intermediario.Bancos import Banco

pedro = Cliente('pedro', '77445588', '33344466678')
maria = Cliente('maria', '99885533', '11111111111')
polly = Cliente('pollyana', '99885533', '11111111111')
conta_pedro = Conta(pedro, 500)
conta_maria = Conta(maria, 5000)
conta_polly = ContaEspecial(polly, 2500, 500)
banco_python = Banco('banco python', '003')

banco_python.abrir_conta(conta_pedro)
banco_python.abrir_conta(conta_polly)
banco_python.abrir_conta(conta_maria)

banco_python.lista_contas()

print(banco_python)

