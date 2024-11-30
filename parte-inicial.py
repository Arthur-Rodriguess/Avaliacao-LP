#INÍCIO DA PARTE DO ARTHUR
from os import system
from time import sleep
#FEITO TAMBÉM ALGUMAS MODIFICAÇÕES NO CÓDIGO GERAL
#FIM DA PARTE DO ARTHUR

system('cls')

#INÍCIO DA PARTE DA JAMILE

#DECLARANDO LISTA DE ALUNOS
lista_alunos = []

#FUNÇÃO MENU 1
def menu_introdutorio():
    sleep(0.3)
    print("\033[1mSeja bem vindo ao nosso sistema de academia!!\033[m")
    sleep(0.3)
    print("Digite uma das opções abaixo: ")
    sleep(0.3)
    print("\033[1m1 - CADASTRO\033[m")
    sleep(0.3)
    print("\033[1m0 - ENCERRAR PROGRAMA\033[m")
    sleep(0.3)
    opcao = int(input("Digite sua escolha: "))
    
    if opcao == 1:
        system('cls')
        print("\033[33mCARREGANDO...\033[m")
        sleep(1)
        system('cls')
        cadastrar_alunos()
        menu_inicial()
        
    elif opcao == 0:
        print("programa encerrado")
        
    else:
        print("\033[31mNúmero inválido\033[m")
            
#FIM DA PARTE DA JAMILE            

#INÍCIO DA PARTE DA JANIELY
#FUNÇÃO CADASTRAR ALUNOS
def cadastrar_alunos():
    qtd_alunos = int(input("Digite a quantidade de alunos que você quer cadastrar: "))
    system('cls')
    
    for aluno in range(qtd_alunos):
        adicionar_aluno = input("\033[1mDigite o nome do Aluno(a):\033[m ")
        lista_alunos.append(adicionar_aluno)
        system('cls')
        print(f"\033[32mAluno(a) \033[1m{adicionar_aluno}\033[m\033[32m cadastrado com sucesso!!\033[m")
        sleep(1.5)
        system('cls')
        
#FUNÇÃO REMOVER ALUNOS
def remover_alunos():
    print("\033[1mAlunos cadastrados:\033[m")
    for indice, aluno in enumerate(lista_alunos):
        sleep(0.5)
        print(f"\033[1m{indice}\033[m - \033[1m{aluno}\033[m")
        
    sleep(0.4)
    print("Digite como você quer remover o Aluno:  ")
    print("\033[1m1 - Pelo Nome")
    print("2 - Pelo Código\033[m")
    print("3 - Voltar ao Menu Inicial")
    print("4 - Sair do Programa")
    opcao_remover_alunos = int(input("Digite: "))
    
    if opcao_remover_alunos == 1:
        qtd_alunos_remover = int(input("Digite a quantidade de Alunos que você quer remover: "))
        
        for alunos_remover in range(0, qtd_alunos_remover):
            remover_aluno = input("Digite o nome do Aluno(a) que você quer remover: ")
            lista_alunos.remove(remover_aluno)
            system('cls')
            print("CARREGANDO...")
            sleep(1)
            system('cls')
            print(f"\033[32mAluno \033[1m{remover_aluno}\033[m\033[32m removido com sucesso!!\033[m")
            
    elif opcao_remover_alunos == 2:
        qtd_alunos_remover = int(input("Digite a quantidade de Alunos que você quer remover: "))
        
        for alunos_remover in range(0, qtd_alunos_remover):
            indice_aluno = int(input("Digite o código do Aluno(a) que você quer remover: "))
            nome_aluno = lista_alunos[indice_aluno]
            lista_alunos.remove(nome_aluno)
            print(f"Aluno \033[1m{nome_aluno}\033[m removido com sucesso!!")

    elif opcao_remover_alunos == 3:
        print("Você voltou ao Menu Inicial!")

    elif opcao_remover_alunos == 4:
        print("Programa Encerrado!")

    else:
        print("Digito Inválido/Voltar ao Menu Inicial!") 

#FUNÇÃO ATUALIZAR ALUNOS            
def atualizar_alunos():
    print("\033[1mAlunos cadastrados:\033[m")
    for indice, aluno in enumerate(lista_alunos):
        sleep(0.5)
        print(f"\033[1m{indice} - \033[1m{aluno}")
        
    sleep(0.4)    
    print("Digite como você quer atualizar o aluno: ")       
    print("1 - Pelo Nome")
    print("2 - Pelo Código")
    print("3 - Voltar ao Menu Inicial")
    print("4 - Sair do Programa")
    opcao_atualizar_aluno = int(input("Digite: "))
    
    if opcao_atualizar_aluno == 1:
        qtd_alunos_atualizar = int(input("Digite a quantidade de alunos que você quer atualizar: "))
        
        for alunos_atualizar in range(0, qtd_alunos_atualizar):
            buscar_aluno = input("Digite o nome do(a) aluno(a) para atualizar: ")
            atualizar_aluno = input("Digite o nome do novo aluno(a): ")
        
            for indice, aluno in enumerate(lista_alunos):
                if buscar_aluno == aluno:
                    lista_alunos[indice] = atualizar_aluno
                    print(f"\033[32mAluno(a) \033[1m{atualizar_aluno}\033[m\033[32m atualizado com sucesso!!\033[m")
                    break
                    
    elif opcao_atualizar_aluno == 2:
        qtd_alunos_atualizar = int(input("Digite a quantidade de alunos que você quer atualizar: "))
        
        for alunos_atualizar in range(0, qtd_alunos_atualizar):
            buscar_aluno = int(input("Digite o código do(a) aluno(a) para atualizar: "))
            nome_desatualizado_aluno = lista_alunos[buscar_aluno]
            
            nome_atualizado_aluno = str(input("Digite o nome do novo aluno(a): "))
            for indice, aluno in enumerate(lista_alunos):
                if indice == buscar_aluno:
                    lista_alunos[indice] = nome_atualizado_aluno
                    print(f"Aluno(a) \033[1m{nome_desatualizado_aluno}\033[m Atualizado para \033[1m{nome_atualizado_aluno}\033[m")
    
    elif opcao_atualizar_aluno  == 3:
        print("Você voltou ao Menu Inicial!")
    
    elif opcao_atualizar_aluno == 4:
        print("Programa Encerrado!")
    
    else:
        print("Digito Inválido/Voltar ao Menu Inicial!")

#FUNÇÃO LISTAR ALUNOS        
def listar_alunos():
    for indice, aluno in enumerate(lista_alunos):
        print(f"Código do Aluno(a): \033[1m{indice}\033[m Aluno(a): \033[1m{aluno}\033[m ")
        
#FIM DA PARTE DA JANIELY  

#INÍCIO DA PARTE DA MARIA DE FATIMA

#FUNÇÃO MENU INICIAL 
def menu_inicial():
    while True:
        print("\033[1mSISTEMA DE ACADEMIA\033[m")
        sleep(0.3)
        print("\033[1m1 - CADASTRAR MAIS ALUNOS\033[m")
        sleep(0.3)
        print("\033[1m2 - ATUALIZAR\033[m")
        sleep(0.3)
        print("\033[1m3 - REMOVER\033[m")
        sleep(0.3)
        print("\033[1m4 - LISTAR\033[m")
        sleep(0.3)
        print("\033[1m0 - SAIR DO PROGRAMA\033[m")
        sleep(0.3)
        
        opcao = int(input("Digite uma das opções aqui: "))
        sleep(0.3)
        system('cls')
        
        if opcao == 1:
            print("\033[33mCARREGANDO...\033[m")
            sleep(1.5)
            system('cls')
            cadastrar_alunos()
            
        elif opcao == 2:
            print("\033[33mCARREGANDO...\033[m")
            sleep(1.5)
            system('cls')
            atualizar_alunos()
            
        elif opcao == 3:
            print("\033[33mCARREGANDO...\033[m")
            sleep(1.5)
            system('cls')
            remover_alunos()
            
        elif opcao == 4:
            print("\033[33mCARREGANDO...\033[m")
            sleep(1.5)
            system('cls')
            listar_alunos()
            
        elif opcao == 0:
            print("Programa Encerrado!")
            break
            
        else:
            print("Número Inválido/Voltar ao Menu!")
            
#INICIALIZAÇÃO DO PROGRAMA
menu_introdutorio()

#FIM DA PARTE DA MARIA DE FATIMA