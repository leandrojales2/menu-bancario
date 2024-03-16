def menu():
    menu = """

    [c] Cadastrar Conta
    [u] Cadastrar Usuário
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return menu

def cadastrar_conta(cpf, agencia, numero_conta, saldo_inicial):
    print("Cadastro de Conta")
    cpf = input("Informe o CPF para Cadastro da conta (somente números): ")
    for numero_cpf in usuarios_cadastrados: 
        if numero_cpf["cpf"] == cpf:

            if contas_cadastradas is None:
                numero_conta = "1"
                print(numero_conta)
            else:
                numero_conta = len(contas_cadastradas) + 1

            agencia = "0001"

            if numero_conta in contas_cadastradas:
                input("Número de já cadastrada")
            
            else:
                saldo_inicial = float(input("Digite o saldo inicial da conta: "))
                contas_cadastradas.append(({"cpf": cpf, "agencia": agencia, "numero_conta": numero_conta, "saldo_inicial": saldo_inicial}))
                print("Conta cadastrada com Sucesso!")

            return  cpf, agencia, numero_conta, saldo_inicial 
        
        else:
            print("O CPF Informado ainda não possui cadastro.")
            return None, None, None, None

def cadastrar_usuario(cpf, nome, data_nascimento, endereco):
    cpf = input("Digite seu CPF (somente números): ")
    for numero_cpf in usuarios_cadastrados: 
        if numero_cpf["cpf"] == cpf:
            print("CPF já cadastrado. Por favor, reinicie a operação.")
            return None, None, None, None

    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereco (logradouro, numero - bairro - cidade/uf): ")
    usuarios_cadastrados.append(({"cpf": cpf, "agencia": agencia, "numero_conta": numero_conta, "saldo_inicial": saldo_inicial}))
    print(f'Usuário Cadastrado')
        
    return nome, data_nascimento, cpf, endereco

def depositar(saldo, depositos_realizados):
    print("Informe o valor que deseja depositar: ")
    deposito = float(input())
    if deposito > 0:
        saldo += deposito
        depositos_realizados.append(deposito)
        print(f'Depósito no valor de R$ {deposito:.2f} realizado!')
        print(f'Seu saldo atual é de R$ {saldo:.2f}.')
    else:
        print("Valor menor ou igual a 0. Depósito não realizado!")
    return saldo, depositos_realizados

def saque(saldo, numero_saques, limite_saques, saques_realizados):
    if numero_saques < limite_saques:
        print("Informe o valor que deseja sacar: ")
        valor_saque = float(input())
        if valor_saque > 500:
            print("Valor digitado é maior que o limite diário permitido por saque.")
        else:
            if valor_saque <= saldo:
                if valor_saque > 0:
                    saques_realizados.append(valor_saque)
                    saldo -= valor_saque
                    print(f'Saque no valor de R$ {valor_saque:.2f} realizado!')
                    print(f'Seu saldo atual é de R$ {saldo:.2f}.')
                    numero_saques += 1
                else:
                    print("Valor digitado não é válido. Favor retorne à operação.")
            else:
                print("Valor do saque é maior que o limite disponível.")
    else:
        print("Limite diário de saque atingido!")
    return saldo, numero_saques, saques_realizados

def extrato(saldo, saldo_inicial, depositos_realizados, saques_realizados):
    print(f"Extrato Bancário\n")
    print(f"Saldo Inicial:     | R$  {saldo_inicial:.2f}\n")
    print("Tipo de Operação   | Valor")
    print("---------------------------------------")

    for valor in depositos_realizados:
        print(f"Depósito           | R$  {valor:.2f}\n")

    for valor in saques_realizados:
        print(f"Saque              | R$ {-(valor):.2f}\n")

    print(f'Seu saldo atual é de R$  {saldo:.2f}.')
    print("---------------------------------------\n")

saldo = 0
limite = 500
deposito = 0
numero_saques = 0
limite_saques = 3
valor_saque = 0
depositos_realizados = []
saques_realizados = []
tipo_operacao = ""
saldo_inicial = 0
usuarios_cadastrados = []
contas_cadastradas = []
endereco = ""
agencia = 0
numero_conta = 0
numero_cpf = ""
usuario = ""

while True:

    opcao = input(menu())

    if opcao == "c":
       cpf, agencia, numero_conta, saldo_inicial = cadastrar_conta(cpf, agencia, numero_conta, saldo_inicial)
    
    elif opcao == "u":
        cpf, nome, data_nascimento, endereco = cadastrar_usuario(cpf, nome, data_nascimento, endereco)

    elif opcao == "d":
        saldo, depositos_realizados = depositar(saldo, depositos_realizados)

    elif opcao == "s":
        saldo, numero_saques, saques_realizados = saque(saldo, numero_saques, limite_saques, saques_realizados)

    elif opcao == "e":
        extrato(saldo, saldo_inicial, depositos_realizados, saques_realizados)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")