#AQUI COMEÇA A PARTE CENTRAL - RESPONSÁVEL PELO ESTUDANTE PEDRO GABRIEL ABREU DE LIMA

#FUNÇÃO DA LISTA DE EXERCÍCIOS DO PRÓPRIO ALUNO
lista_exercicios = []

#FUNÇÕES DOS EXERCÍCIOS
#FUNÇÃO DOS EXERCÍCIOS PARA SUPERIOR:

#FUNÇÃO DOS EXERCÍCIOS PARA OMBRO
def exercicios_ombro():
    print("Aqui está os exercícios para ombro: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Elevação Unilateral Inclinada")
    print("2 - Abdução Ombro Polia")
    print("3 - Elevação Lateral Sentada")
    print("4 - Elevação Frontal Unilateral Polia")
    print("5 - Face Pull")
    print("6 - Elevação Frontal Corda Polia")
    print("7 - Desenvolvimento Harnold")
    print("8 - Desenvolvimento Halteres")
    print("9 - Elevação Unilateral")
    print("10 - Elevação Frontal Halteres")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Elevação Unilateral Inclinada") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Abdução Ombro Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Elevação Lateral Sentada")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Elevação Frontal Unilateral Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Face Pull")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Elevação Frontal Corda Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Desenvolvimento Harnold")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Desenvolvimento Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Elevação Unilateral")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Elevação Frontal Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS DE PEITORAL
def exercicios_peitoral():
    print("Aqui está os exercícios para peitoral: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Crucifixo Cross Halteres Baixa")
    print("2 - Crucifixo Alternado Cross Polia Baixa")
    print("3 - Mergulho em Barra Paralelas")
    print("4 - Crucifixo Cross Polia Média")
    print("5 - Crucifixo Supino Reto")
    print("6 - Supino Inclinado Barra")
    print("7 - Supino Inclinado Halteres")
    print("8 - Crucifixo Cross Polia Alta")
    print("9 - Supino Reto Halteres")
    print("10 - Crucifixo Halteres Supino Declinado")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Crucifixo Cross Halteres Baixa") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Crucifixo Alternado Cross Polia Baixa")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Mergulho em Barra Paralelas")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Crucifixo Cross Polia Média")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Crucifixo Supino Reto")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Supino Inclinado Barra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Supino Inclinado Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Crucifixo Cross Polia Alta")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Supino Reto Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Crucifixo Halteres Supino Declinado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS DE COSTAS
def exercicios_costas():
    print("Aqui está os exercícios para costas: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)
    
#FUNÇÃO DE EXERCÍCIOS DE BÍCEPS
def exercicios_biceps():
    print("Aqui está os exercícios para costas: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA TRÍCEPS
def exercicios_triceps():
    print("Aqui está os exercícios para costas: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA TRAPÉZIO
def exercicios_trapezio():
    print("Aqui está os exercícios para costas: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios_proprios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA ANTEBRAÇO
def exercicios_antebraco():
    print("Aqui está os exercícios para costas: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios_proprios.append(seu_exercicio)

#FUNÇÕES DE EXERCÍCIOS PARA POSTERIOR:

#FUNÇÃO DE EXERCÍCIOS PARA QUADRÍCEPS
def exercicios_quadriceps():
    print("Aqui está os exercícios para quadriceps: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios_proprios.append(seu_exercicio)

#FUNÇAO DE EXERCÍCIOS PARA ISQUIOTIBIAIS
def exercicios_isquiotibiais():
    print("Aqui está os exercícios para isquiotibiais: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios_proprios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA GLÚTEO
def exercicios_gluteos():
    print("Aqui está os exercícios para gluteos: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre esses? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA PANTURRILHA
def exercicios_panturrilha():
    print("Aqui está os exercícios para panturrilha: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre esses? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÕES DE EXERCÍCIOS PARA PRÁTICA PRÓPRIA (SEM AUXÍLIO DE MÁQUINAS)

#FUNÇÃO DE EXERCÍCIOS PARA ABDOMEN
def exercicios_abdomen():
    print("Aqui está os exercícios para abdomen: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre esses? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA FUNCIONAIS
def exercicios_funcionais():
    print("Aqui está os exercícios para funcionais: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre esses? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA AEROBIOS
def exercicios_aerobios():
    print("Aqui está os exercícios para aerobios: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre esses? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA MOBILIDADE
def exercicios_mobilidade():
    print("Aqui está os exercícios para mobilidade: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre esses? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA EXERCÍCIO LIVRE
def exercicios_exercicios_livres():
    print("Aqui está os exercícios para exercícios livres: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre esses? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DE EXERCÍCIOS PARA LIBERAÇÃO MIOFASCIAL
def exercicios_liberacao_miofascial():
    print("Aqui está os exercícios para liberação miofascial: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append(" ") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append(" ")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

    print("Seu exercício não se encontra entre esses? Digite você mesmo o seu: ")
    seu_exercicio = str(input("Digite o seu exercício: "))
    lista_exercicios.append(seu_exercicio)

#FUNÇÃO DO CRONOGRAMA DE TREINOS
def cronograma_academia():
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
    print("16 - Exercício livres")
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
cronograma_academia()

