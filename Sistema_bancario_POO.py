class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class ContaCorrente:
    def __init__(self, numero, cliente, agencia="0001", limite=500, limite_saques=3):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = ""
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Limite de saques diários atingido.")
        elif valor > self.limite:
            print("O valor do saque ultrapassa o limite permitido por operação.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para saque.")

    def mostrar_extrato(self):
        print("\n=== EXTRATO ===")
        print(self.extrato if self.extrato else "Nenhuma movimentação.")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def buscar_cliente_por_cpf(self, cpf):
        return next((cliente for cliente in self.clientes if cliente.cpf == cpf), None)

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        if self.buscar_cliente_por_cpf(cpf):
            print("Já existe um usuário com esse CPF.")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

        novo_cliente = Cliente(nome, cpf, data_nascimento, endereco)
        self.clientes.append(novo_cliente)
        print("Usuário criado com sucesso!")

    def criar_conta(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = self.buscar_cliente_por_cpf(cpf)

        if not cliente:
            print("Cliente não encontrado. Crie o usuário antes de criar a conta.")
            return

        numero_conta = len(self.contas) + 1
        conta = ContaCorrente(numero=numero_conta, cliente=cliente)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)

        print(f"Conta criada com sucesso! Agência: {conta.agencia}, Conta: {conta.numero}")

    def selecionar_conta(self):
        cpf = input("Informe o CPF do titular da conta: ")
        cliente = self.buscar_cliente_por_cpf(cpf)
        if cliente and cliente.contas:
            return cliente.contas[0]  # para simplificação, retorna a primeira conta
        print("Cliente ou conta não encontrada.")
        return None

    def menu(self):
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
                conta = self.selecionar_conta()
                if conta:
                    valor = float(input("Informe o valor do depósito: "))
                    conta.depositar(valor)

            elif opcao == "s":
                conta = self.selecionar_conta()
                if conta:
                    valor = float(input("Informe o valor do saque: "))
                    conta.sacar(valor)

            elif opcao == "e":
                conta = self.selecionar_conta()
                if conta:
                    conta.mostrar_extrato()

            elif opcao == "nu":
                self.criar_usuario()

            elif opcao == "nc":
                self.criar_conta()

            elif opcao == "q":
                print("Obrigado por usar nosso sistema bancário.")
                break

            else:
                print("Opção inválida. Tente novamente.")


# Executar sistema
if __name__ == "__main__":
    banco = Banco()
    banco.menu()
