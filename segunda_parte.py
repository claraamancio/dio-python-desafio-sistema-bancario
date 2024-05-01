menu = """
########  MENU  ######## 
#   [1] Depósito       #
#   [2] Saque          # 
#   [3] Extrato        #
#   [4] Nova Conta     #
#   [5] Listar Contas  #
#   [6] Novo Usuário   #
#   [7] Sair           #
########################
"""

def saque(*, saldo, valor_sacado, extrato, limite, numero_de_saques, limite_de_saques):
    saldo_insuficiente = saldo < valor_sacado
    limite_excedido = valor_sacado > limite
    numero_de_saques_excedido = numero_de_saques >= limite_de_saques
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
    return saldo, extrato

def deposito(saldo, valor_depositado, extrato, /):
    if valor_depositado > 0:
        saldo += valor_depositado
        extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido! Não foi possível completar a operação!")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n################ EXTRATO ################")
    if not extrato:
        print("Não foram realizadas movimentações.\n")
    else:
        print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("#########################################")

def criar_usuario(clientes):
    cpf = input("Informe seu cpf: ")
    filtro_cliente = [cliente for cliente in clientes if cliente["cpf"]==cpf]
    if filtro_cliente:
        print("Cliente já cadastrado!")
        return
    nome = input("Informe seu nome completo: ")
    data_de_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereço = input("Informe seu endereço (logradouro, número - bairro - cidade/sigla estado): ")
    clientes.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereço": endereço})
    print("Cliente cadastrado com sucesso!")

def criar_conta(agencia, numero_da_conta, clientes):
    cpf = input("Informe o seu cpf: ")
    filtro_cliente = [cliente for cliente in clientes if cliente["cpf"]==cpf]
    if filtro_cliente:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_da_conta": numero_da_conta, "usuario": filtro_cliente[0]}
    print("Cliente não cadastrado! Realize seu cadastro!")

def listar_contas(contas):
    for conta in contas:
        mensagem = f"""
        Agência: {conta["agencia"]}
        C/C: {conta["numero_da_conta"]}
        Titular: {conta["usuario"]["nome"]}

        """
        print(mensagem)

def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    numero_de_saques = 0
    clientes = []
    contas = []
    numero_da_conta = 1
    limite = 500

    while True:
        print(menu)
        acao = int(input("Insira a ação desejada: "))
        if acao == 1:
            valor_depositado = float(input("Informe o valor a ser depositado: "))
            saldo, extrato = deposito(saldo, valor_depositado, extrato)
        elif acao == 2:
            valor_sacado = float(input("Insira o valor a ser sacado: ")) 
            saldo, extrato = saque(saldo=saldo, valor_sacado=valor_sacado, extrato=extrato, limite=limite,numero_de_saques=numero_de_saques, limite_de_saques=LIMITE_DE_SAQUES)
        elif acao == 3:
            exibir_extrato(saldo, extrato=extrato)
        elif acao == 4:
            conta = criar_conta(AGENCIA, numero_da_conta, clientes)
            if conta:
                contas.append(conta)
                numero_da_conta += 1
        elif acao == 5:
            listar_contas(contas)
        elif acao == 6:
            criar_usuario(clientes)
        elif acao == 7:
            break
        else:
            print("Operação inválida! Tente novamente!")
    
main()













