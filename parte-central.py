#AQUI COMEÇA A PARTE CENTRAL - RESPONSÁVEL PELO ESTUDANTE PEDRO GABRIEL ABREU DE LIMA

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

#FUNÇÕES DO MENU DA PARTE CENTRAL
#FUNÇÃO ATUALIZAR TREINOS CADASTRADOS PELO PRÓPRIO ALUNO
def atualizar_treino():
    print("Quer atualizar um treino?")
    print("Digite o meio pelo qual removerá o treino: ")
    print("1 - Pelo Nome")
    print("2 - Pelo Código")
    print("3 - Encerrar Programa")
    print("4 - Voltar ao Menu Central")
    opcao_atualizar_treino = int(input("Digite uma das opções: "))

    if opcao_atualizar_treino == 1:
        nome_treino = str(input("Digite o nome do treino que você quer remover: "))
        nome_atualizado_treino = str(input("Digite o novo nome do treino: "))
        lista_exercicios(nome_treino) = nome_atualizado_treino
        print(f"O treino {nome_treino} atualizado para {nome_atualizado_treino}")

    elif opcao_atualizar_treino == 2:
        indice_treino = int(input("Digite o código do treino que você quer remover: "))
        nome_atualizado_treino = str(input("Digite o novo nome para o treino: "))
        lista_exercicios[indice_treino] = nome_atualizado_treino
        print(f"Treino {lista_exercicios[indice_treino]} atualizado para {nome_atualizado_treino}")

    elif opcao_atualizar_treino == 3:
        print("Função Atualizar Treinos Encerrada!")

    elif opcao_atualizar_treino == 4:
        print("Você voltou ao menu central!")


#FUNÇÃO REMOVER TREINOS
def remover_treino():
    print("Então você está decidido em remover um treino, certo? Pois bem, comece: ")
    print("Digite o meio que usará para remover seu treino: ")
    print("1 - Pelo Nome")
    print("2 - Pelo Código")
    print("3 - Encerrar Programa")
    print("4 - Voltar ao Menu Central")
    opcao_remover_aluno = int(input("Digite uma das opções: "))

    if opcao_remover_aluno == 1:
        nome_treino = str(input("Digite o nome do treino: "))
        lista_exercicios.remove(nome_treino)
        print(f"Treino {nome_treino} removido com sucesso!")

    elif opcao_remover_aluno == 2:
        indice_treino = int(input("Digite o indice do treino: "))
        lista_exercicios.remove(indice_treino)
        print(f"{lista_exercicios[indice_treino]} removido com sucesso!")

    elif opcao_remover_aluno == 3:
        print("Função Remover Treinos Encerrada!")

    elif opcao_remover_aluno == 4:
        print("Você voltou ao menu central!")

#FUNÇÃO BUSCAR TREINOS
def buscar_treino():
    print("Agora, vamos buscar algum treino que você deseja: ")
    indice_treino = int(input("Primeiramente, digite o 'código' do seu treino: "))
    nome_treino = lista_exercicios[indice_treino]
    print(f"O treino buscado foi: {nome_treino}")

#FUNÇÃO LISTAR TREINOS
def listar_treino():
    for treino in lista_exercicios:
        print(f"Seus treinos cadastrados até então são: {lista_exercicios}")

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