import os

# Declarando variáveis globais

saldo = 0
valor = 0 
total_depositos = 0
total_saques = 0
mensagem_boas_vindas = f'''
---------------------------------------------------------------------------

Bem-vindo ao sistema bancário! Por favor, escolha uma opção:

1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Extrato bancário
0 - Sair

---------------------------------------------------------------------------
'''

# Funções do sistema bancário
def consultar_saldo(saldo):
    print(f"\n Seu saldo atual é: R$ {saldo:.2f}")

def depositar(saldo, total_depositos):
    valor = float(input("\n Digite o valor a ser depositado: "))
    saldo += valor
    total_depositos += valor
    print(f"\n Depósito realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
    return saldo, total_depositos

def sacar(saldo, total_saques):
    valor = float(input("\n Digite o valor a ser sacado: "))
    if valor <= saldo:
        saldo -= valor
        total_saques += valor
        print(f"\n Seu saldo atual é: R$ {saldo:.2f}")
        return saldo, total_saques
    else:
        print("\n Saldo insuficiente.")
        return saldo, total_saques

def sair():
    print("\n Obrigado por utilizar o sistema bancário. Até logo!")
    exit()
    
def extrato_bancario(saldo, total_depositos, total_saques):
    mensagem_extrato = f'''
    --------------------------------------------------------------------------- 
    Seu historico de transações:
    Saldo atual: R$ {saldo:.2f} 
    Seu total de depósitos: R$ {total_depositos:.2f}
    Seu total de saques: R$ {total_saques:.2f}  
    ---------------------------------------------------------------------------

    '''
    print(mensagem_extrato)

# Loop principal do sistema bancário
while True:
    
    escolha = input(mensagem_boas_vindas)
    os.system('cls')

    if escolha == "1":
        consultar_saldo(saldo)
    elif escolha == "2":
        saldo, total_depositos = depositar(saldo, total_depositos)
    elif escolha == "3":
        saldo, total_saques = sacar(saldo, total_saques)
    elif escolha == "4":
        extrato_bancario(saldo, total_depositos, total_saques)    
    elif escolha == "0":
        sair()
    else:
        print("Opção inválida.")
        
    input("\n Pressione Enter para continuar...")