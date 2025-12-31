import textwrap

from datetime import datetime
from functools import wraps

def log_transacao(func):
     @wraps(func)
     def wrapper(*args, **kwargs):
          data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          print(f'[LOG] {data_hora} | Transação: {func.__name__}')
          #print(f"[LOG] {data_hora} | Transação: {func.__name__.replace('_', ' ').title()}")
          return func(*args, **kwargs)
     return wrapper

def menu():
    menu = """
Lista de opções! \n
[u] Criar Usuário
[c] Criar Conta Corrente
[l] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    return input(textwrap.dedent(menu))

@log_transacao
def criar_usuario(usuarios):
     
     nome= input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     cpf = input("Informe o CPF (somente números): ")
     endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
     for usuario in usuarios:
          if usuario["cpf"] == cpf:
               print("Já existe um usuário com esse CPF!")
               return
     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
     #print(f"Usuário criado com sucesso!{usuarios}")
     return usuarios

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def filtar_contas(numero_conta,cpf):
        contas_filtradas = [conta for conta in contas if conta["numero_conta"] == numero_conta and conta["usuario"]["cpf"] == cpf]
        return contas_filtradas[0] if contas_filtradas else None

def listar_contas(usuarios):
     for conta in contas:
          usuario = filtrar_usuario(conta["usuario"]["cpf"], usuarios)
          print(f"Agencia: {conta['agencia']}")
          print(f"Conta: {conta['numero_conta']}")
          print(f"Titular: {usuario['nome']}")
          print("")

@log_transacao
def criar_conta_corrente(usuarios, agencia,contas):
      numero_conta = len(contas) + 1
      cpf = input("Informe o CPF do usuário: ")
      usuario = filtrar_usuario(cpf, usuarios)
      if usuario:
           contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
           print("Conta criada com sucesso!")
      else:
           print("Usuário não encontrado, fluxo de criação de conta encerrado!")

@log_transacao
def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

@log_transacao
def sacar(*, saldo, valor, extrato, numero_saques, limite, limite_saques):
    limite = saldo

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    else:
            print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato,numero_saques

def exibir_extrato(saldo,*,extrato):
      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("==========================================")
      return saldo, extrato

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    global contas
    contas = []
    

    while True:
        opcao = menu()

        if opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            criar_conta_corrente(usuarios= usuarios, contas= contas, agencia= AGENCIA)

        elif opcao == "l":
            listar_contas(usuarios)

        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(valor, saldo, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                numero_saques=numero_saques,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()