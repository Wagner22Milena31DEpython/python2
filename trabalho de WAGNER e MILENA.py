import os
conta = []
saldo = []
proprietario = []

def deletar():
    os.system('cls')

def cadastrar(numero,donodaconta):
    conta.append(numero)
    saldo.append(0)
    proprietario.append(donodaconta) 
    return "sua conta foi cadastrada com sucesso"

def verificar():
     cont = 0
     while cont < len(conta):
        print("propietario:", (proprietario[cont]),"\t",  "numero da conta: ", (conta[cont]), "\t", "saldo:", saldo[cont], )
        cont +=  1

def deposito(numero):
   if numero in conta:
       valor = float(input("Digite o valor do deposito      "))
       posicao = conta.index(numero)
       saldo[posicao] = (saldo[posicao]) + valor       
       return "deposito realizado com sucesso"
   else:
       return "Conta Inexistente"

def saque(numero):
    if numero in conta:
       valor = float(input("Digite o valor a ser sacado     "))
       posicao = conta.index(numero)
       saldo[posicao] = (saldo[posicao]) - valor       
       return "saque realizado com sucesso"
    else:
       return "Conta Inexistente"

def transferencia(numero1,valortrans1,numero2):
    if numero1 in conta:
        posicao = conta.index(numero1)
        saldo[posicao] = (saldo[posicao]) - valortrans1   
    else:
        print("conta inexistente")
        if numero2 in conta:
            posicao2 = conta.index(numero2)
            saldo[posicao2] = (saldo[posicao2]) + valortrans1
        else:
            print("conta inexistente")

op = 1
while op != 0:
    op = int(input("bom dia senhor(a), no que nosso banco pode lhe ajudar?"+
              "\n1 - cadastrar uma conta"+
              "\n2 - verificar seu saldo"+
              "\n3 - adicionar dinheiro ao saldo"+
              "\n4 - deseja sacar seu dinheiro?"+
              "\n5 - deseja realizar uma transferencia"+
              "\n0 - encerrar"
              "\n então, o que o(a) senhor(a) deseja?     "))
    if op == 1:
         deletar()
         num = int(input("por favor,digite um numero para sua conta    "))
         dono = str(input("digite seu nome por gentileza    "))
         cadastrar(num,dono)
         print("seu saldo atual neste momento é 0")
    elif op == 2:
        verificar()
    elif op == 3:        
        deletar()
        numeroConta = int(input("me diga por favor, qual o numero da sua conta      "))
        deposito(numeroConta)
    elif op == 4:
        deletar()
        numeroConta2 = int(input("me diga por favor, qual o numero da sua conta      "))
        saque(numeroConta2)
    elif op == 5:
        deletar()
        num = int(input("digite o numero da conta que deseja transferir o dinheiro    "))
        valortrans2 = float(input("Digite o valor a ser transferido    "))
        alvodatransferencia = int(input("digite o numero da conta para qual deseja transferir    "))
        transferencia(num,valortrans2,alvodatransferencia)