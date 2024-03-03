menu = """
Seja Bem vindo ao Banco Jales!

Digite a operação que deseja realizar.

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
        
indice = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
deposito = 0
valor_saque = 0
depositos_realizados = []
saques_realizados = []
tipo_operacao = ""
saldo_inicial = 0

while True:
  opcao = input(menu)

  if opcao == "d":
    print("Informe o valor que deseja depositar. " )
    deposito = float(input())
    if deposito > 0:
        saldo += deposito
        depositos_realizados.append(deposito)
        print(f'Deposito no valor de R$ {deposito:.2f} realizado!')
        print(f'Seu saldo atual é de R$ {saldo:.2f}.')

    else:
        print("Valor menor ou igual a 0, Deposito não realizado!")

  elif opcao == "s":

    if numero_saques <= limite_saques:
       
        print("Informe o valor que deseja sacar. " )
        valor_saque = float(input())

        if valor_saque > 500:
          print("Valor digitado maior que o limite diário, permitido por saque.")

        else:

          if valor_saque <= saldo:
            
              if valor_saque > 0:
                  saques_realizados.append(valor_saque)
                  saldo -= valor_saque
                  print(f'Saque no valor de R$ {valor_saque:.2f} realizado!')
                  print(f'Seu saldo atual é de R$ {saldo:.2f}.')
                  numero_saques += 1
              
              else:
                
                print("Valor digitado não é válido, favor retome a operação.")
          
          else:
            
            print("Valor do saque é maior que limite disponível.")

    else:
       print("Limite diário de saque atingido!")
  
  elif opcao == "e":
    indice = 0
    print(f"Extrato Bancário\n")
    print(f"Saldo Inicial:     | R$  {saldo_inicial:.2f}\n")
    print("Tipo de Operação   | Valor")
    print("---------------------------------------")

    percorrer_deposito = len(depositos_realizados)
    for transacao in range(0, percorrer_deposito):
        valor = depositos_realizados[indice]
        print(f"Depósito           | R$  {valor:.2f}\n")
        indice += 1

    indice = 0

    percorrer_saque = len(saques_realizados)
    for transacao in range(0, percorrer_saque):
        valor = saques_realizados[indice]
        print(f"Saque              | R$ {-(valor):.2f}\n")
        indice += 1

    print(f'Seu saldo atual é de R$  {saldo:.2f}.')
    print("---------------------------------------\n")

  elif opcao == "q":
    break
  
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada")