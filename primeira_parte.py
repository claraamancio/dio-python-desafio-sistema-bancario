menu = """
######## MENU ######## 
#   [1] Depósito     #
#   [2] Saque        # 
#   [3] Extrato      #
#   [4] Sair         #
######################
"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    print(menu)
    acao = int(input("Insira a ação desejada: "))
    
    # Depósito
    if acao == 1:
        valor_depositado = float(input("Informe o valor a ser depositado: "))
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido! Não foi possível completar a operação!")
    
    # Saque
    elif acao == 2:
        valor_sacado = float(input("Insira o valor a ser sacado: ")) 
        saldo_insuficiente = saldo < valor_sacado
        limite_excedido = valor_sacado > limite
        numero_de_saques_excedido = numero_de_saques >= LIMITE_DE_SAQUES
        if saldo_insuficiente:
            print("Saldo insuficiente! Não foi possível completar a operação!")       
        elif limite_excedido:
            print("Limite de saque excedido! Não foi possível completar a operação!")
        elif numero_de_saques_excedido:
            print("Número de saques excedido! Não foi possível completar a operação!")
        elif valor_sacado > 0:
            saldo -= valor_sacado
            extrato += f"Saque: R$ {valor_sacado:.2f}\n"
            numero_de_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido! Não foi possível completar a operação!")

    # Extrato
    elif acao == 3:
        print("\n################ EXTRATO ################")
        if not extrato:
            print("Não foram realizadas movimentações.\n")
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("#########################################")

    # Sair
    elif acao == 4:
        print("Obrigado pela preferência! Volte sempre!")
        break
    
    # Caso ação for diferente de 1, 2, 3 ou 4
    else:
        print("Operação inválida! Tente novamente!")