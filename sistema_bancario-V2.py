menu = """\n
------------------------MENU------------------------

-- Bem vindo ao banco, informe o que queira fazer :

[d]  Depositar
[s]  Sacar
[e]  Exibir extrato
[u]  Criar novo usuario
[nc] Criar nova conta
[f]  Sair
--->"""
LIMITE_SAQUES = 3
AGENCIA ="0001"
saldo =0
limite =500
extrato =" "
numero_saques =0
usuarios =[]
contas =[]
numero_conta =0

def depositar(saldo, valor, extrato ,/):

    if valor > 0 :
        saldo += valor
        extrato += f"Depósito :R${valor:.2f}"
        print(f"depósito realizado com sucesso!! este é o seu saldo atual {saldo}") 
    else:
        print("Falha ao realizar o depósito!!!")    


    return saldo, extrato    

def sacar(* , saldo, valor, numero_saques, limite_saques, extrato, limite):
    atingiu_limite= limite < valor
    atingiu_limite_saques = limite_saques < numero_saques
    saldo_insuficiente = valor > saldo
    
    if atingiu_limite:
        print("****** Voçê atingiu o limite do valor de saque!!! ******")
       
    elif atingiu_limite_saques:
        print("####### Voçê atingiu o limite de saques diários!!!! #######")

    elif saldo_insuficiente:
        print(" Voçê não tem saldo suficiente para completar este saque!!!!")   
 
    elif valor > 0:
        print ("realizando saque!!")   
        saldo -= valor
        extrato += f"saque :R${valor:.2f}"    
        print(f"saque realizado com sucesso, seu saldo atual é de {saldo}")
       

    else:
        print("Falha ao realizar o saque , Por favor tente novamente mais tarde!!!") 
       

    return saldo, extrato   

def criar_usuario(usuarios):
    cpf = int(input("Informe o seu cpf(somente números):"))
    usuario = Verificar_usuarios(cpf,usuarios)
    print("Criação de usuário iniciada!!!")
    if usuario:
        print("Usuário já existente!!!!")
        return

    nome=input("informe o seu nome completo:")
    cidade=input("informe seu endereço(incluindo = longradura-numero-bairro-cidade/sigla do estado):")
    data_nascimento=input("informe sua data de nascimento(Dia/Mês/Ano):")

    usuarios.append({"nome":nome ,"cidade":cidade , "data de nascimeto":data_nascimento})
    
    print("----Usuário criado com sucesso-----")
    return

def Verificar_usuarios(cpf, usuarios):
    usuarios_verificados = []
   
    for usuario in usuarios:
        if cpf == cpf:
            usuarios_verificados.append(usuario)

    return usuarios_verificados[0] if usuarios_verificados else None

def criar_conta (agencia , numero_conta, usuarios):
    cpf=int(input("Informe o seu cpf(somente números):"))
    usuario=Verificar_usuarios(cpf,usuarios)
    print("Criação de conta iniciada!!")
    if usuario:
        print("Conta criada com sucesso")
        return {"agência":agencia,"número da conta":numero_conta , "usuario":usuario }
    else:
        print("\n-------Usuário não encontrato , criação de conta encerrada!!!!-------") 

def exibir_extrato(saldo, /, *, extrato):

    print("-------|EXTRATO|-------")
    if extrato:
        print(extrato)  
        print(f"\nSaldo : R${saldo:.2f}")
        print("-----------Esse é o seu extrato----------")

    else:
        print("Não ouve movimentações na sua conta")
    return extrato   

while True: 
    alternativa=input(menu)

    if alternativa =="d":
        print(f"Seu saldo atual é de {saldo}!!!")

        valor =int(input("informe o valor do depósito:")) 

        saldo, extrato = depositar(saldo, valor, extrato)

    elif alternativa =="s":
        print(f"Seu saldo atual é de {saldo}!!!")

        valor = int(input("informe o valor que voçê queira sacar:"))
        
        numero_saques += 1 

        saldo, extrato = sacar(
            saldo = saldo ,
            valor = valor ,
            numero_saques = numero_saques ,
            limite_saques = LIMITE_SAQUES ,
            extrato = extrato ,
            limite = limite ,
            )

    elif alternativa =="e":
        exibir_extrato(saldo, extrato = extrato)

    elif alternativa=="u":
        criar_usuario(usuarios)

    elif alternativa=="nc":
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        numero_conta = len(contas)+1
           
            
        if conta:
            contas.append(conta)

    elif alternativa=="f":
        print("Obrigado por usar o nosso banco!!!")
        break
    
    else:
        print("operação ínvalida, tente outra operação!!!!")
