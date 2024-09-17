menu = """

[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
        opcao = input(menu)

        if opcao == "a":
            valor = float(input("informe o valor do depósito: "))

            if valor > 0:
                  saldo += valor
                  extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                  print("Operação falhow! o valor informado é inválido.")

        elif opcao == "b":
            valor = float(input("Informe o valor do saque: ")) 

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! o valor do saque excede o limite.")

            elif excedeu_saques: 
                print("Operação falhou! Você excedeu o limite de saques diários")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1    

            else:                             
                print("Operação falhou! O valor informado é inválido.")
 
        elif opcao == "c":
            print("\n================ EXTRATO ================")
            print("Não fomra realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("===========================================")
            
        elif opcao == "d":
             break

        else:
             print("Operação inválida, por favor selecione novamente a operação desejada")    