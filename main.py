#AQUI COMEÇA A PARTE GERAL (MODIFICAÇÕES EM TODO O CÓDIGO MAIS OUTRAS 'DECORAÇÕES') - RESPONSÁVEL PELO ESTUDANTE ARTHUR RODRIGUES DE FREITAS Nº06
from os import system
from time import sleep
#FEITO TAMBÉM ALGUMAS MODIFICAÇÕES NO CÓDIGO GERAL
#FIM DA PARTE DO ARTHUR

#PARTE DA MODULARIZAÇÃO (PEGANDO FUNÇÕES DA funcoes_parte_central.py E TRAZENDO PARA ESSA, main.py)
from funcoes_parte_central import *
#TÉRMINO DA PARTE DA MODULARIZAÇÃO

#AQUI COMEÇA A PARTE CENTRAL - RESPONSÁVEL PELOS ESTUDANTES JAMILE GONÇALVES, JANIELY RIBEIRO, MARIA DE FATIMA Nº15, 16, 30
system('cls')

#INÍCIO DA PARTE DA JAMILE
#DECLARANDO LISTA DE ALUNOS
lista_alunos = []

#FUNÇÃO MENU 1
def menu():
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
        cadastrar()
        menu2()
        
    elif opcao == 0:
        print("programa encerrado")
        
    else:
        print("\033[31mNúmero inválido\033[m")
            
#FIM DA PARTE DA JAMILE            

#INÍCIO DA PARTE DA JANIELY
#FUNÇÃO CADASTRAR ALUNOS
def cadastrar():
    qtd_alunos = int(input("Digite a quantidade de alunos que você quer cadastrar: "))
    system('cls')
    
    for aluno in range(qtd_alunos):
        adicionar_aluno = input("\033[1mDigite o nome do Aluno(a):\033[m ")
        lista_alunos.append(adicionar_aluno)
        system('cls')
        print(f"\033[32mAluno(a) {adicionar_aluno} cadastrado com sucesso!!\033[m")
        sleep(1.5)
        system('cls')
        
#FUNÇÃO REMOVER ALUNOS
def remover():
    print("\033[1mAlunos cadastrados:\033[m")
    for indice, aluno in enumerate(lista_alunos):
        sleep(0.5)
        print(f"{indice} - {aluno}")
        
    sleep(0.4)
    print("Digite como você quer remover o Aluno:  ")
    print("1 - Pelo Nome")
    print("2 - Pelo Código")
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
            print(f"Aluno {remover_aluno} removido com sucesso!!")
            
    if opcao_remover_alunos == 2:
        qtd_alunos_remover = int(input("Digite a quantidade de Alunos que você quer remover: "))
        
        for alunos_remover in range(0, qtd_alunos_remover):
            indice_aluno = int(input("Digite o código do Aluno(a) que você quer remover: "))
            nome_aluno = lista_alunos[indice_aluno]
            lista_alunos.remove(nome_aluno)
            print(f"Aluno {nome_aluno} removido com sucesso!!")
            
#FUNÇÃO ATUALIZAR ALUNOS            
def atualizar():
    print("\033[1mAlunos cadastrados:\033[m")
    for indice, aluno in enumerate(lista_alunos):
        sleep(0.5)
        print(f"{indice} - {aluno}")
        
    sleep(0.4)    
    print("Digite como você quer remover o aluno: ")       
    print("1 - Pelo Nome")
    print("2 - Pelo Código")
    opcao_atualizar_aluno = int(input("Digite: "))
    
    if opcao_atualizar_aluno == 1:
        qtd_alunos_atualizar = int(input("Digite a quantidade de alunos que você quer atualizar: "))
        
        for alunos_atualizar in range(0, qtd_alunos_atualizar):
            buscar_aluno = input("Digite o nome do(a) aluno(a) para atualizar: ")
            atualizar_aluno = input("Digite o nome do novo aluno(a): ")
        
            for indice, aluno in enumerate(lista_alunos):
                if buscar_aluno == aluno:
                    lista_alunos[indice] = atualizar_aluno
                    print(f"\033[32mAluno(a) {atualizar_aluno} atualizado com sucesso!!\033[m")
                    break
                    
    if opcao_atualizar_aluno == 2:
        qtd_alunos_atualizar = int(input("Digite a quantidade de alunos que você quer atualizar: "))
        
        for alunos_atualizar in range(0, qtd_alunos_atualizar):
            buscar_aluno = int(input("Digite o código do(a) aluno(a) para atualizar: "))
            nome_desatualizado_aluno = lista_alunos[buscar_aluno]
            
            nome_atualizado_aluno = str(input("Digite o nome do novo aluno(a): "))
            for indice, aluno in enumerate(lista_alunos):
                if indice == buscar_aluno:
                    lista_alunos[indice] = nome_atualizado_aluno
                    print(f"Aluno(a) {nome_desatualizado_aluno} Atualizado para {nome_atualizado_aluno}")
                    
#FUNÇÃO LISTAR ALUNOS        
def listar():
    for indice, aluno in enumerate(lista_alunos):
        print(f"Código do Aluno(a): {indice} Aluno(a): {aluno} ")
        
#FIM DA PARTE DA JANIELY  

#INÍCIO DA PARTE DA MARIA DE FATIMA
#FUNÇÃO MENU 2
def menu2():
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
            cadastrar()
            
        elif opcao == 2:
            print("\033[33mCARREGANDO...\033[m")
            sleep(1.5)
            system('cls')
            atualizar()
            
        elif opcao == 3:
            print("\033[33mCARREGANDO...\033[m")
            sleep(1.5)
            system('cls')
            remover()
            
        elif opcao == 4:
            print("\033[33mCARREGANDO...\033[m")
            sleep(1.5)
            system('cls')
            listar()
            
        elif opcao == 0:
            print("Obrigado por utilizar o nosso programa!!")
            break
            
        else:
            print("número inválido/voltar ao menu")
            
#INICIALIZAÇÃO DO PROGRAMA
menu()
#FIM DA PARTE DA MARIA DE FATIMA

#AQUI COMEÇA A PARTE CENTRAL - RESPONSÁVEL PELO ESTUDANTE PEDRO GABRIEL ABREU DE LIMA Nº38

#ESTA LINHA DE CÓDIGO FAZ COM QUE PEGUE TUDO O QUE TEM NA PÁGINA funcoes_parte_central.py E TRAGA PARA ESTA parte-central.py
from funcoes_parte_central import *

#TAMBÉM PODERIA TER SIDO USADO DESSA FORMA:
# from funcoes_parte_central import exercicios_ombro, exercicios_peitoral, exercicios_costas, exercicios_biceps, exercicios_triceps, exercicios_trapezio, exercicios_antebraco, exercicios_quadriceps, exercicios_isquiotibiais, exercicios_gluteos, exercicios_panturrilha, exercicios_abdomen, exercicios_funcionais, exercicios_aerobios, exercicios_mobilidade, exercicios_exercicios_livres, exercicios_liberacao_miofascial

#FUNÇÃO DO CRONOGRAMA DE TREINOS
def cronograma_treinos_academia():
    while True:
        print("Seja bem vindo ao Cronograma da Academia!")
        print("Preciso que você primeiramente digite qual membro irá trabalhar para que eu possa lhe entregar os exercícios cabíveis.")
        print("<--Aqui são os treinos para superior:-->")
        print("1 - Ombro")
        print("2 - Peitoral")
        print("3 - Costas")
        print("4 - Bíceps")
        print("5 - Tríceps")
        print("6 - Trapezio")
        print("7 - Antebraço")

        print("<--Aqui são os treinos para posterior:-->")
        print("8 - Quadríceps")
        print("9 - Isquiotibiais")
        print("10 - Glúteos")
        print("11 - Panturrilha")

        print("<--Aqui começa os exercícios por parte física e não por musculação-->")
        print("12 - Abdomen")
        print("13 - Funcionais")
        print("14 - Aerobios")
        print("15 - Mobilidade")
        print("16 - Exercícios livres")
        print("17 - Liberação miofascial")
        opcao = int(input("Digite: "))

        if opcao == 1:
            exercicios_ombro()
        elif opcao == 2:
            exercicios_peitoral()
        elif opcao == 3:
            exercicios_costas()
        elif opcao == 4:
            exercicios_biceps()
        elif opcao == 5:
            exercicios_triceps()
        elif opcao == 6:
            exercicios_trapezio()
        elif opcao == 7:
            exercicios_antebraco()
        elif opcao == 8:
            exercicios_quadriceps()
        elif opcao == 9:
            exercicios_isquiotibiais()
        elif opcao == 10:
            exercicios_gluteos()
        elif opcao == 11:
            exercicios_panturrilha()
        elif opcao == 12:
            exercicios_abdomen()
        elif opcao == 13:
            exercicios_funcionais()
        elif opcao == 14:
            exercicios_aerobios()
        elif opcao == 15:
            exercicios_mobilidade()
        elif opcao == 16:
            exercicios_exercicios_livres()
        elif opcao == 17:
            exercicios_liberacao_miofascial()
        else:
            print("DIGITO INVÁLIDO/VOLTAR AO MENU CENTRAL")

#INICIALIZAÇÃO DO PROGRAMA DE CRONOGRAMA COM A FUNÇÃO DE CRONOGRAMA DE TREINOS
cronograma_treinos_academia()

#COLOCANDO MENU NA PARTE CENTRAL

#MENU DA PARTE CENTRAL
def menu_parte_central():
    while True:
        print("Navegue pelos seus treinos e muito mais:")
        print("1 - Volte ao Menu Inicial")
        print("2 - Cadastrar mais Treinos")
        print("3 - Atualizar Treinos")
        print("4 - Remover Treinos")
        print("5 - Buscar Treino")
        print("6 - Listar Treinos")
        opcao = int(input("Digite sua escolha: "))

        # if opcao == 1:
            # menu()
        if opcao == 2:
            cronograma_treinos_academia()
        elif opcao == 3:
            atualizar_treino()
        elif opcao == 4:
            remover_treino()
        elif opcao == 5:
            buscar_treino()
        elif opcao == 6:
            listar_treino()
        else:
            print("DIGITO INVÁLIDO/VOLTAR AO MENU")