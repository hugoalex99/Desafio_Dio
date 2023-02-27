saldo = 0
limite = 500
extrato = ''
numero_saques = 1
LIMITE_SAQUES = 3
saque = 0
total_saque = 0
total_deposito = 0

while True:

    menu = print('''
--------------------
[Banco do Brasil]
[Escolha uma opção!]

[d] = Depositar
[s] = sacar
[e] = Extrato
[q] = Sair
''')

    opcao = input('Digite a opção desejada: ')

    if opcao == 'd':
        print('\nVocê escolheu Depósito')
        saldo = float(input('Qual valor de Deposito: '))

        if saldo > 0:
            print('\nValor Depositado com sucesso!!')
            total_deposito = saldo + total_deposito
            #saldo = total_deposito - saque
        else:
            print('\nTente Novamente, Voltamos ao menu inicial!!')
               

    elif opcao == 's':  
        print('\nVocê escolheu Sacar')
        saque = float(input('Digite o valor de saque: R$ '))
        saldo = saldo - saque

        if saldo <= limite and numero_saques <= LIMITE_SAQUES and saldo >= 0 and limite >= saque:
            numero_saques = numero_saques + 1
            print(f'Saque de R$ {saque:.2f}')
            print('Número de saque diário: ',numero_saques - 1)
            total_saque = saque + total_saque 

        elif saldo < 0:
            saldo = saque + saldo   
            print(f'Saldo insuficiente para saque!!!: Saldo - R$ {saldo:.2f}')  

        elif saque > limite:
            saldo = saque + saldo
            print('Você ultrapassou o Limite de saque diário!!!')
            
        elif LIMITE_SAQUES < numero_saques:
            saldo = saque + saldo
            print(f'Limite de saques diários excedidos!')     

    elif opcao == 'e':
        deposito = total_saque + saldo
        print('\nVocê escolheu Extrato')
        print('\nExtrato Bancário')
        print(f'\nDepositos feitos  R$.....{total_deposito:.2f}')
        print(f'\nSaques realizados R$....{total_saque:.2f}')
        print(f'\nNúmeros de Saques diários:> ', numero_saques - 1)
        print(f'\nSaldo Disponível  R$.....{saldo:.2f}')

    elif opcao == 'q':
        print('\nVocê escolheu sair!!!')
        break

    else:
        print('\nOpção inválida! Tente novamente')         

