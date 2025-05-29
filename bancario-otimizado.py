def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario_existente = any(usuario["cpf"] == cpf for usuario in usuarios)
    if usuario_existente:
        print("Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Crie um usuário antes de criar a conta.")
        return

    numero_conta = len(contas) + 1
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Número da conta: {numero_conta}")


def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato


def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))

    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    elif valor > limite:
        print("O valor do saque ultrapassa o limite permitido por operação (R$ 500).")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido para saque.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n=== EXTRATO ===")
    print("Nenhuma movimentação." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        print("\n=== MENU ===")
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[nu] Novo Usuário")
        print("[nc] Nova Conta")
        print("[q] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            criar_conta(AGENCIA, contas, usuarios)

        elif opcao == "q":
            print("Obrigado por usar esse sistema bancário. Até breve!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Executar o programa
main()