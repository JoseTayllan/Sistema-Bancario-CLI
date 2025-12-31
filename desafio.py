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
[r] Relatório de Transações
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
           contas.append({
                "agencia": agencia, 
                "numero_conta": numero_conta,
                "usuario": usuario,
                "saldo": 0.0,
                "transacoes": []
                })
           print("Conta criada com sucesso!")
      else:
           print("Usuário não encontrado, fluxo de criação de conta encerrado!")

@log_transacao
def deposito(valor, saldo, extrato, transacoes):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        transacoes.append({
             "tipo": "deposito", 
             "valor": valor
             })
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

@log_transacao
def sacar(*, saldo, valor, extrato, numero_saques, limite, limite_saques, transacoes):
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
            transacoes.append({
                    "tipo": "saque",
                    "valor": valor
            })

    else:
            print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato,numero_saques

def exibir_extrato(saldo,*,extrato):
      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("==========================================")
      return saldo, extrato

def gerar_relatorio(transacoes, tipo=None):
    """
    Gerador de relatório de transações.
    :param transacoes: lista de transações
    :param tipo: 'deposito', 'saque' ou None
    """
    for transacao in transacoes:
        if tipo is None or transacao["tipo"] == tipo:
            yield transacao

class ContaIterador:
     def __init__(self, contas):
          self.contas = contas
          self.indice = 0

     def __iter__(self):
          return self

     def __next__(self): 
          if self.indice >= len(self.contas):
               raise StopIteration
          conta = self.contas[self.indice]
          self.indice += 1

          return{
            "agencia": conta.get("agencia"),
            "numero_conta": conta.get("numero_conta"),
            "usuario": conta.get("usuario", {}).get("nome"),
            "saldo": conta.get("saldo",0.0)
        }
          
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
    transacoes = []
    

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
            saldo, extrato = deposito(valor, saldo, extrato, transacoes)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                numero_saques=numero_saques,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
                transacoes=transacoes
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "r":
            tipo = input("Filtrar por (deposito/saque ou enter para todos): ").lower()
            tipo = tipo if tipo else None

            for t in gerar_relatorio(transacoes, tipo):
                print(f"{t['tipo'].title()} - R$ {t['valor']:.2f}")
                
        elif opcao =="1":
             print("\n=== Contas do banco ===")
             for conta in ContaIterador(contas):
                 print(
                     f"Agência: {conta['agencia']} | "
                     f"Conta: {conta['numero_conta']} | "
                     f"Titular: {conta['usuario']} | "
                     f"Saldo: R$ {conta['saldo']:.2f}"
                 )
             print("=======================\n")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()