saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\n=== MENU ===")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        elif valor > limite:
            print("O valor do saque ultrapassa o limite permitido por operação (R$ 500).")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n=== EXTRATO ===")
        print("Nenhuma movimentação." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Obrigado por usar esse sistema bancário. Até breve!")
        break

    else:
        print("Opção inválida. Tente novamente.")
