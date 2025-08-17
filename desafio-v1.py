"""
O desafio tem por objetivo a implementação simples de um sistema bancário
"""
from codecs import strict_errors

menu = """
Informe a letra correspondete a operação desejada:

[d] → para depósitos
[s] → para sacar
[e] → para ver o extrato
[q] → para sair

"""

saldo = 0
limite_valor_saque = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Qual valor deseja depositar? '))

        if valor > 0:
            saldo += valor #soma ao saldo atual o valor do deposito realizado
            extrato += f'+ R$ {valor:.2f}\n'
        else:
            print('O valor deve ser maior que zero! Verifique e tente novamente.')

    elif opcao == 's':
        valor = float(input('Quanto deseja sacar? '))

        if valor > saldo:
            print('Valor desejado é maior que o saldo! Operação cancelada.')
        elif valor > limite_valor_saque:
            print('Valor limite de saque excedido! Operação cancelada.')
        elif numero_saques == LIMITE_SAQUES:
            print('Quantidade de saques excedida! Operação cancelada.')
        elif valor <= 0:
            print('O valor deve ser maior que zero! Operação cancelada.')
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f'- R$ {valor:.2f}\n'

    elif opcao == 'e':
        str_extrato = f"""
######### EXTRATO BANCÁRIO #########
Movimentações (+ → depósitos; - → saques):
{extrato}
Saldo: R$ {saldo:.2f}
####################################
        """
        str_extrato_sem_movimento = 'Não foram realizadas movimentações.'

        if extrato:
            print(str_extrato)
        else:
            print(str_extrato_sem_movimento)

    elif opcao == 'q':
        break

    else:
        print('Operação inválida! Por favor, tente novamente.')