#AQUI SE INICIA A CHAMADA DE BIBLIOTECAS PARA ALTERAÇÃO NA ESTILIZAÇAO DO CÓDIGO - RESPONSÁVEL PELO ESTUDANTE ARTHUR RODRIGUES DE FREITAS Nº06
from time import sleep
from os import system

#AQUI COMEÇA A PARTE CENTRAL - RESPONSÁVEL PELO ESTUDANTE PEDRO GABRIEL ABREU DE LIMA Nº38

#ESTA LINHA DE CÓDIGO FAZ COM QUE PEGUE TUDO O QUE TEM NA PÁGINA funcoes_parte_central.py E TRAGA PARA ESTA parte-central.py
from funcoes_parte_inicial import *
from funcoes_parte_central import *
#TAMBÉM PODERIA TER SIDO USADO DESSA FORMA:
# from funcoes_parte_central import exercicios_ombro, exercicios_peitoral, exercicios_costas, exercicios_biceps, exercicios_triceps, exercicios_trapezio, exercicios_antebraco, exercicios_quadriceps, exercicios_isquiotibiais, exercicios_gluteos, exercicios_panturrilha, exercicios_abdomen, exercicios_funcionais, exercicios_aerobios, exercicios_mobilidade, exercicios_exercicios_livres, exercicios_liberacao_miofascial

#FUNÇÃO DO CRONOGRAMA DE TREINOS
def cronograma_treinos_academia():
    print("Seja bem vindo ao Cronograma da Academia!")
    print("Preciso que você primeiramente digite qual membro irá trabalhar para que eu possa lhe entregar os exercícios cabíveis.")
    print("<--Aqui são os treinos para superior:-->")
    print("\033[1m1 - Ombro")
    print("2 - Peitoral")
    print("3 - Costas")
    print("4 - Bíceps")
    print("5 - Tríceps")
    print("6 - Trapezio")
    print("7 - Antebraço\033[m")
    sleep(0.3)

    print("<--Aqui são os treinos para posterior:-->")
    print("\033[1m8 - Quadríceps")
    print("9 - Isquiotibiais")
    print("10 - Glúteos")
    print("11 - Panturrilha\033[m")
    sleep(0.3)

    print("<--Aqui começa os exercícios por parte física e não por musculação-->")
    print("\033[1m12 - Abdomen")
    print("13 - Funcionais")
    print("14 - Aerobios")
    print("15 - Mobilidade")
    print("16 - Exercícios livres")
    print("17 - Liberação miofascial\033[m")
    sleep(0.3)

    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        exercicios_ombro()
        
    elif opcao_treino == 2:
        exercicios_peitoral()
        
    elif opcao_treino == 3:
        exercicios_costas()
        
    elif opcao_treino == 4:
        exercicios_biceps()
        
    elif opcao_treino == 5:
        exercicios_triceps()
        
    elif opcao_treino == 6:
        exercicios_trapezio()
        
    elif opcao_treino == 7:
        exercicios_antebraco()
        
    elif opcao_treino == 8:
        exercicios_quadriceps()
        
    elif opcao_treino == 9:
        exercicios_isquiotibiais()
        
    elif opcao_treino == 10:
        exercicios_gluteos()
        
    elif opcao_treino == 11:
        exercicios_panturrilha()
        
    elif opcao_treino == 12:
        exercicios_abdomen()
        
    elif opcao_treino == 13:
        exercicios_funcionais()
        
    elif opcao_treino == 14:
        exercicios_aerobios()
        
    elif opcao_treino == 15:
        exercicios_mobilidade()
        
    elif opcao_treino == 16:
        exercicios_exercicios_livres()
        
    elif opcao_treino == 17:
        exercicios_liberacao_miofascial()
        
    else:
        print("DIGITO INVÁLIDO/VOLTAR AO MENU CENTRAL")

#INICIALIZAÇÃO DO PROGRAMA DE CRONOGRAMA COM A FUNÇÃO DE CRONOGRAMA DE TREINOS
cronograma_treinos_academia()

#COLOCANDO MENU NA PARTE CENTRAL

#MENU DA PARTE CENTRAL
def gerenciamento_treinos():
    while True:
        print(f"Navegue pelos seus treinos e muito mais:")
        print("1 - Volte ao Menu Inicial")
        print("2 - Cadastrar mais Treinos")
        print("3 - Atualizar Treinos")
        print("4 - Remover Treinos")
        print("5 - Buscar Treino")
        print("6 - Listar Treinos")
        print("7 - Trocar de Usuário")
        print("0 - Encerrar Programa")
        opcao = int(input("Digite sua escolha: "))

        if opcao == 1:
            print("Você voltou ao Menu Inicial!")
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
            trocar_usuario()
            
        else:
            print("DIGITO INVÁLIDO/VOLTAR AO MENU")
            


    
