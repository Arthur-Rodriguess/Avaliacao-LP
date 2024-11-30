#NESTA PARTE, VOCÊ ENCONTRARÁ A PARTE DE TODO MUNDO EM UM SÓ LUGAR!

#AQUI COMEÇA A PARTE GERAL (MODIFICAÇÕES EM TODO O CÓDIGO MAIS OUTRAS 'DECORAÇÕES')
from os import system
from time import sleep

#PARTE DA MODULARIZAÇÃO (PEGANDO FUNÇÕES DA funcoes_parte_central.py E TRAZENDO PARA ESSA, main.py)
from funcoes_parte_central_inicial import *
#TÉRMINO DA PARTE DA MODULARIZAÇÃO

system('cls')

#DECLARANDO LISTA DE ALUNOS
lista_alunos = []

#FUNÇÃO MENU INICIAL
def menu_inicial():
    while True:
        print("\033[1mSISTEMA DE ACADEMIA - GERENCIAMENTO DE ALUNOS\033[m")
        sleep(0.3)
        print("\033[1m1 - CADASTRAR MAIS ALUNOS\033[m")
        sleep(0.3)
        print("\033[1m2 - ATUALIZAR ALUNOS\033[m")
        sleep(0.3)
        print("\033[1m3 - REMOVER ALUNOS\033[m")
        sleep(0.3)
        print("\033[1m4 - LISTAR ALUNOS\033[m")
        sleep(0.3)
        print("\033[1m5 - IR PARA O GERENCIAMENTO DE TREINOS\033[m")
        sleep(0.3)
        print("\033[1m6 - ADICIONAR TREINOS DO ALUNO\033[m")
        sleep(0.3)
        print("\033[1m0 - ENCERRAR PROGRAMA\033[m")
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
        
        elif opcao == 5:
            print("\033[33mCARREGANDO...\033[m")
            sleep(1.5)
            system('cls')
            menu_central()
        
        elif opcao == 6:
            print("\033[33mCARREGANDO...\033[m")
            sleep(1.5)
            system('cls')
            cronograma_treinos_academia()

        elif opcao == 0:
            print("Obrigado por utilizar o nosso programa!!")
            break
            
        else:
            print("número inválido/voltar ao menu")

#MENU DA PARTE CENTRAL
def menu_central():
    while True:
        print("SISTEMA DE ACADEMIA - GERENCIAMENTO DE TREINOS:")
        print("1 - VOLTE AO MENU INICIAL")
        print("2 - CADASTRAR MAIS TREINOS")
        print("3 - ATUALIZAR TREINOS")
        print("4 - REMOVER TREINOS")
        print("5 - BUSCAR TREINOS")
        print("6 - LISTAR TREINOS")
        print("7 - VOLTAR AO MENU INICIAL")
        print("0 - ENCERRAR PROGRAMA")
        opcao = int(input("Digite sua escolha: "))

        if opcao == 1:
            menu_inicial()

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

        elif opcao == 7:
            print("Você voltou ao Menu Inicial!")
            menu_inicial()

        elif opcao == 0:
            print("Programa Encerrado!")
            break

        else:
            print("DIGITO INVÁLIDO/VOLTAR AO MENU INICIAL")
            menu_inicial()

#FUNÇÃO DO CRONOGRAMA DE TREINOS
def cronograma_treinos_academia():
    print("Seja bem vindo ao Cronograma de treinos da Academia!")
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
    print("18 - Voltar ao Menu Central")
    print("0 - Encerrar Programa")
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

    elif opcao == 18:
        print("Você voltou ao Menu Central!")

    elif opcao == 0:
        print("Programa Encerrado!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO MENU CENTRAL")

#INICIALIZAÇÃO DO PROGRAMA
menu_introdutorio()