#AQUI COMEÇA A PARTE CENTRAL - RESPONSÁVEL PELO ESTUDANTE PEDRO GABRIEL ABREU DE LIMA Nº38

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
    print("11 - Seu exercício não se encontra?")
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
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")
        
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
    print("11 - Seu exercício não se encontra?")
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
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS DE COSTAS
def exercicios_costas():
    print("Aqui está os exercícios para costas: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Crucifixo Inverso Polia")
    print("2 - Remada Unilateral Polia Alta")
    print("3 - Crucifixo Inverso Banco")
    print("4 - Remada Baixa Neutra")
    print("5 - Remada Smith Pronada")
    print("6 - Remada Curvada Polia")
    print("7 - Pulley Frente Neutro")
    print("8 - Puxada Frontal Pegada Neutra Aberta")
    print("9 - Pulley Trás")
    print("10 - Pulley Triângulo")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Crucifixo Inverso Polia") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Remada Unilateral Polia Alta")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Crucifixo Inverso Banco")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Remada Baixa Neutra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Remada Smith Pronada")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Remada Curvada Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Pulley Frente Neutro")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Puxada Frontal Pegada Neutra Aberta")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Pulley Trás")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Pulley Triângulo")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")
    
#FUNÇÃO DE EXERCÍCIOS DE BÍCEPS
def exercicios_biceps():
    print("Aqui está os exercícios para bíceps: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Rosca Spider Halteres")
    print("2 - Rosca Concentrada")
    print("3 - Rosca Unilateral Polia Alta")
    print("4 - Rosca Direta Banco 45 (Graus)")
    print("5 - Rosca Spider Barra")
    print("6 - Rosca Direta na Polia Baixa com Corda")
    print("7 - Rosca Alternada Sentado")
    print("8 - Rosca Scott com Barra 'H'")
    print("9 - Rosca Direta Barra")
    print("10 - Rosca Direta Barra H")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Rosca Spider Halteres") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Rosca Concentrada")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Rosca Unilateral Polia Alta")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Rosca Direta Banco 45 (Graus)")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Rosca Spider Barra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Rosca Direta na Polia Baixa com Corda")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Rosca Alternada Sentado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Rosca Scott com Barra 'H'")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Rosca Direta Barra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Rosca Direta Barra H")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA TRÍCEPS
def exercicios_triceps():
    print("Aqui está os exercícios para tríceps: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Tríceps Testa Máquina")
    print("2 - Tríceps Mergulho Livre")
    print("3 - Tríceps Coíse Unilateral")
    print("4 - Tríceps Coíse Pegada Neutra")
    print("5 - Tríceps Máquina")
    print("6 - Tríceps Pulley Barra W")
    print("7 - Tríceps Francês Barra")
    print("8 - Tríceps Francês Barra W")
    print("9 - Tríceps Testa Polia Corda")
    print("10 - Tríceps Francês Halteres Unilateral")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Tríceps Testa Máquina") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Tríceps Mergulho Livre")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Tríceps Coíse Unilateral")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Tríceps Coíse Pegada Neutra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Tríceps Máquina")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Tríceps Pulley Barra W")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Tríceps Francês Barra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Tríceps Francês Barra W")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Tríceps Testa Polia Corda")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Tríceps Francês Halteres Unilateral")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA TRAPÉZIO
def exercicios_trapezio():
    print("Aqui está os exercícios para trapezio: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Encolhimento de Ombro pela Frente Barra")
    print("2 - Encolhimento de Ombro Barra Atrás")
    print("3 - Encolhimento de Ombro Halteres")
    print("4 - Face Pull")
    print("5 - Remada Alta Anilha")
    print("6 - Remada Alta Polia")
    print("7 - Elevação Escapular")
    print("8 - Remada Alta Barra")
    print("9 - Adução Escapula Polia Baixa")
    print("10 - Remada Alta Barra")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Encolhimento de Ombro pela Frente Barra") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Encolhimento de Ombro Barra Atrás")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Encolhimento de Ombro Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Face Pull")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Remada Alta Anilha")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Remada Alta Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Elevação Escapular")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Remada Alta Barra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Adução Escapula Polia Baixa")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Remada Alta Barra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA ANTEBRAÇO
def exercicios_antebraco():
    print("Aqui está os exercícios para antebraço: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Antebraço Máquina")
    print("2 - Lenhador")
    print("3 - Rosca Punho Halteres")
    print("4 - Rosca Direta Giro Inverso Halteres")
    print("5 - Rosca Inversa Polia")
    print("6 - Rosca Inversa Halteres")
    print("7 - Rosca Punho Barra")
    print("8 - Rosca Punho")
    print("9 - Rosca Punho Polia Sentado")
    print("10 - Giro Punho")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Antebraço Máquina") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Lenhador")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Rosca Punho Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Rosca Direta Giro Inverso Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Rosca Inversa Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Rosca Inversa Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Rosca Punho Barra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Rosca Punho")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Rosca Punho Polia Sentado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Giro Punho")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÕES DE EXERCÍCIOS PARA POSTERIOR:

#FUNÇÃO DE EXERCÍCIOS PARA QUADRÍCEPS
def exercicios_quadriceps():
    print("Aqui está os exercícios para quadriceps: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Afundo Barra Livre")
    print("2 - Afundo com Halteres")
    print("3 - Afundo com Step")
    print("4 - Afundo com Step + Afundo")
    print("5 - Afundo Smith")
    print("6 - Afundo Suspendo Smith")
    print("7 - Agachamento Barra")
    print("8 - Agachamento Frontal + Sumô Halteres")
    print("9 - Agachamento Frontal Halteres")
    print("10 - Agachamento Halteres Lateral")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Afundo Barra Livre") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Afundo com Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Afundo com Step")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Afundo com Step + Afundo")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Afundo Smith")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Afundo Suspendo Smith")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Agachamento Barra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Agachamento Frontal + Sumô Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Agachamento Frontal Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Agachamento Halteres Lateral")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇAO DE EXERCÍCIOS PARA ISQUIOTIBIAIS
def exercicios_isquiotibiais():
    print("Aqui está os exercícios para isquiotibiais: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Stiff Halteres Step")
    print("2 - Stiff Polia Baixa")
    print("3 - Flexor Deitado com Halteres")
    print("4 - Mesa Flexora Unilateral")
    print("5 - Stiff Polia Baixa com Step")
    print("6 - Hiperextensão Lombar")
    print("7 - Stiff Smith")
    print("8 - Extensão Glúteo Polia")
    print("9 - Stiff com Step")
    print("10 - Posterior Harck")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Stiff Halteres Step") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Stiff Polia Baixa")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Flexor Deitado com Halteres")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Mesa Flexora Unilateral")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Stiff Polia Baixa com Step")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Hiperextensão Lombar")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Stiff Smith")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Extensão Glúteo Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Stiff com Step")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Posterior Harck")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA GLÚTEO
def exercicios_gluteos():
    print("Aqui está os exercícios para glúteos: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Abdução Máquina Pé")
    print("2 - Glúteo Máquina 4 Apoio Pé")
    print("3 - Abdução Polia")
    print("4 - Extensão + Flexão Quadril Caneleira")
    print("5 - Glúteo Máquina 4 Apoio Deitado")
    print("6 - Extensão Quadril Polia Banco")
    print("7 - Extensão Quadril Caneleira")
    print("8 - Elevação Pelvica Barra")
    print("9 - Abdução Polia Deitada")
    print("10 - Extensão Quadril Polia")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Abdução Máquina Pé") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Glúteo Máquina 4 Apoio Pé")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Abdução Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Extensão + Flexão Quadril Caneleira")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Glúteo Máquina 4 Apoio Deitado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Extensão Quadril Polia Banco")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Extensão Quadril Caneleira")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Elevação Pelvica Barra")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Abdução Polia Deitada")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Extensão Quadril Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA PANTURRILHA
def exercicios_panturrilha():
    print("Aqui está os exercícios para panturrilha: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Panturrilha Unilateral Step")
    print("2 - Panturrilha Sentado Unilateral")
    print("3 - Panturrilha Pé")
    print("4 - Panturrilha Inclinada Pé")
    print("5 - Panturrilha Smith")
    print("6 - Panturrilha Sentado")
    print("7 - Panturrilha Livre")
    print("8 - Panturrilha Harck Burrinho")
    print("9 - Panturrilha Leg 45 (Graus)")
    print("10 - Panturrilha Sentado Unilateral + Bilateral")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Panturrilha Unilateral Step") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Panturrilha Sentado Unilateral")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Panturrilha Pé")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Panturrilha Inclinada Pé")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Panturrilha Smith")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Panturrilha Sentado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Panturrilha Livre")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Panturrilha Harck Burrinho")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Panturrilha Leg 45 (Graus)")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Panturrilha Sentado Unilateral + Bilateral")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÕES DE EXERCÍCIOS PARA PRÁTICA PRÓPRIA (SEM AUXÍLIO DE MÁQUINAS)

#FUNÇÃO DE EXERCÍCIOS PARA ABDOMEN
def exercicios_abdomen():
    print("Aqui está os exercícios para abdomen: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Abdominal Prancha Unilateral")
    print("2 - Abdominal Oblíquo Banco Cruzado")
    print("3 - Abdominal Supra Polia")
    print("4 - Abdominal Supra Polia Tocando Calcanhar")
    print("5 - Abdominal Prancha")
    print("6 - Abdominal Infra L")
    print("7 - Abdominal Canivete")
    print("8 - Abdominal Canoa")
    print("9 - Abdominal V-Sit com Anilha")
    print("10 - Abdominal com Carga")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Abdominal Prancha Unilateral") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Abdominal Oblíquo Banco Cruzado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Abdominal Supra Polia")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Abdominal Supra Polia Tocando Calcanhar")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Abdominal Prancha")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Abdominal Infra L")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Abdominal Canivete")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Abdominal Canoa")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Abdominal V-Sit com Anilha")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Abdominal com Carga")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA FUNCIONAIS
def exercicios_funcionais():
    print("Aqui está os exercícios para funcionais: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Agacha Press Duplo")
    print("2 - Agacha Lateral")
    print("3 - Aganha + Puxada Frontal")
    print("4 - Agacha Press Alter")
    print("5 - Agachamento com Desenvolvimento")
    print("6 - Corrida Calcanhar")
    print("7 - Passada Alternado Saltando")
    print("8 - Perdigueiro")
    print("9 - Agacha Duplo")
    print("10 - Lenhador")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Agacha Press Duplo") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Agacha Lateral")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Aganha + Puxada Frontal")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Agacha Press Alter")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Agachamento com Desenvolvimento")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Corrida Calcanhar")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Passada Alternado Saltando")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Perdigueiro")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Agacha Duplo")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Lenhador")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA AEROBIOS
def exercicios_aerobios():
    print("Aqui está os exercícios para aerobios: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Eliptio")
    print("2 - Trote")
    print("3 - Transport")
    print("4 - Sprint")
    print("5 - Remo")
    print("6 - Bicicleta")
    print("7 - Corrida Esteira")
    print("8 - Caminhada")
    print("9 - Corrida com Inclinação")
    print("10 - Pular Corda")
    print("11 - Seu exercício não se encontra?")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Eliptio") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Trote")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Transport")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Sprint")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Remo")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Bicicleta")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Corrida Esteira")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Caminhada")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Corrida com Inclinação")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Pular Corda")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA MOBILIDADE
def exercicios_mobilidade():
    print("Aqui está os exercícios para mobilidade: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Alongamento Borboleta com Torção")
    print("2 - Alongamento Adutor-Mão a Frente")
    print("3 - Alongamento Borboleta Torção Sentado")
    print("4 - Mobilidade Quadril de Cócoras")
    print("5 - Alongamento Borboleta Flexão Coluna")
    print("6 - Alongamento Ombro Cruzado")
    print("7 - Mobilidade de Coluna na Prancha")
    print("8 - Alongamento Escorpião")
    print("9 - Rotação de Cotovelo e Braço 4 Apoioo")
    print("10 - Rotação Lombar Sentado")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Alongamento Borboleta com Torção") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Alongamento Adutor-Mão a Frente")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Alongamento Borboleta Torção Sentado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Mobilidade Quadril de Cócoras")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Alongamento Borboleta Flexão Coluna")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Alongamento Ombro Cruzado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Mobilidade de Coluna na Prancha")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Alongamento Escorpião")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Rotação de Cotovelo e Braço 4 Apoio")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Rotação Lombar Sentado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA EXERCÍCIO LIVRE
def exercicios_exercicios_livres():
    print("Aqui está os exercícios para exercícios livres: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Deslocamento Lateral Salto")
    print("2 - Corrida no Lugar")
    print("3 - Deslocamento Lateral Cruzado")
    print("4 - Elevação de Joelho")
    print("5 - Deslocamento Lateral Mão Chão")
    print("6 - Extensão Lombar")
    print("7 - Afundo Isométrico Arranque Braços")
    print("8 - Flexão Fechada")
    print("9 - Afundo")
    print("10 - Agachamento Dentro e Fora")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Deslocamento Lateral Salto") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Corrida no Lugar")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Deslocamento Lateral Cruzado")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Elevação de Joelho")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Deslocamento Lateral Mão Chão")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Extensão Lombar")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Afundo Isométrico Arranque Braços")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Flexão Fechada")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Afundo")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Agachamento Dentro e Fora")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DE EXERCÍCIOS PARA LIBERAÇÃO MIOFASCIAL
def exercicios_liberacao_miofascial():
    print("Aqui está os exercícios para liberação miofascial: ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("Aqui está os exercícios para : ")
    print("Digite o número correspondente para adicionar o seu treino a sua lista: ")
    print("1 - Liberação Lombar")
    print("2 - Liberação Serratil")
    print("3 - Liberação Tensor da Fáscia Lata")
    print("4 - Liberação Panturrilha")
    print("5 - Liberação Psoas")
    print("6 - Liberação Peitoral")
    print("7 - Liberação Glúteo")
    print("8 - Liberação Posterior")
    print("9 - Liberação Quadríceps")
    print("10 - Liberação Fascia Plantar com Bolinha")
    opcao_treino = int(input("Digite: "))

    if opcao_treino == 1:
        lista_exercicios.append("Liberação Lombar") 
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 2:
        lista_exercicios.append("Liberação Serratil")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 3:
        lista_exercicios.append("Liberação Tensor da Fáscia Lata")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 4:
        lista_exercicios.append("Liberação Panturrilha")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 5:
        lista_exercicios.append("Liberação Psoas")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 6:
        lista_exercicios.append("Liberação Peitoral")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 7:
        lista_exercicios.append("Liberação Glúteo")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 8:
        lista_exercicios.append("Liberação Posterior")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 9:
        lista_exercicios.append("Liberação Quadríceps")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 10:
        lista_exercicios.append("Liberação Fascia Plantar com Bolinha")
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")
    elif opcao_treino == 11:
        print("Seu exercício não se encontra entre os principais? Digite você mesmo o seu: ")
        seu_exercicio = str(input("Digite o seu exercício: "))
        lista_exercicios.append(seu_exercicio)
        print(f"Exercício(s) {lista_exercicios} adicionado(s) com sucesso!")

    else:
        print("DIGITO INVÁLIDO/VOLTAR AO CRONOGRAMA DE TREINOS")

#FUNÇÃO DO CRONOGRAMA DE TREINOS
def cronograma_treinos_academia():
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

#AQUI, AS FUNÇÕES DA PARTE INICIAL
#AQUI COMEÇA A PARTE INICIAL - RESPONSÁVEL PELOS ESTUDANTES JAMILE GONÇALVES, JANIELY RIBEIRO E MARIA DE FATIMA
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
    print("\033[1m1 - CADASTRAR ALUNOS\033[m")
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

    elif opcao_atualizar_aluno == 3:
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
        print("\033[1m2 - ATUALIZAR ALUNOS\033[m")
        sleep(0.3)
        print("\033[1m3 - REMOVER ALUNOS\033[m")
        sleep(0.3)
        print("\033[1m4 - LISTAR ALUNOS\033[m")
        sleep(0.3)
        print("\033[3m5 - CADASTRAR TREINOS\033[m")
        sleep(0.3)
        print("\033[3m6 - GERENCIAR TREINOS\033[m")
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
        
        elif opcao == 5:
            print("Sinta-se a vontade para montar seu treino personalizado!")
            cronograma_treinos_academia()
            
        elif opcao == 0:
            print("Obrigado por utilizar o nosso programa!!")
            break
            
        else:
            print("número inválido/voltar ao menu")
            
#INICIALIZAÇÃO DO PROGRAMA
menu_introdutorio()

#FIM DA PARTE DA MARIA DE FATIMA

#FUNÇÕES DO MENU DA PARTE CENTRAL

#FUNÇÃO ATUALIZAR TREINOS CADASTRADOS PELO PRÓPRIO ALUNO OU DA MÁQUINA MESMO
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
        codigo_exercicio = lista_exercicios(nome_treino)
        lista_exercicios[codigo_exercicio] = nome_atualizado_treino
        print(f"O treino {nome_treino} foi atualizado para {nome_atualizado_treino}")

    elif opcao_atualizar_treino == 2:
        indice_treino = int(input("Digite o código do treino que você quer remover: "))
        nome_atualizado_treino = str(input("Digite o novo nome para o treino: "))
        lista_exercicios[indice_treino] = nome_atualizado_treino
        print(f"Treino {lista_exercicios[indice_treino]} atualizado para {nome_atualizado_treino}")

    elif opcao_atualizar_treino == 3:
        print("Função Atualizar Treinos Encerrada!")

    elif opcao_atualizar_treino == 4:
        print("Você voltou ao menu central!")
    
    else:
        print("Digito Inválido/Voltar ao Menu Central!")

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
    
    else:
        print("Número Inválido/Voltar ao Menu Central!")

#FUNÇÃO BUSCAR TREINOS
def buscar_treino():
    print("Agora, vamos buscar algum treino que você deseja: ")
    print("Primeiramente digite como você quer encontrar este treino: ")
    print("1 - Pelo Nome")
    print("2 - Pelo Código")
    print("3 - Voltar ao Menu Central")
    print("4 - Sair do Programa")
    opcao_buscar_alunos = int(input("Digite: "))

    if opcao_buscar_alunos == 1:
        nome_treino = str(input("Digite o nome do seu treino: "))
        lista_exercicios[indice_treino] = nome_treino

        for indice, treino in enumerate(lista_exercicios):
            if treino == nome_treino:
                print("Código do Treino: {indice} Nome do Treino: {treino}")

            else:
                print("Treino não encontrado/Voltar ao Menu Central!")
                
    elif opcao_buscar_alunos == 2:
        indice_treino = int(input("Primeiramente, digite o 'código' do seu treino: "))
        nome_treino = lista_exercicios[indice_treino]
        print(f"O treino buscado foi: {nome_treino}")

    elif opcao_buscar_alunos == 3:
        print("Você voltou ao Menu Central!")

    elif opcao_buscar_alunos == 4:
        print("Programa Encerrado!")

    else:
        print("Digito Inválido/Voltar ao Menu Central!")

#FUNÇÃO LISTAR TREINOS
def listar_treino():
    for treino in lista_exercicios:
        print(f"Seus treinos cadastrados até então são: {lista_exercicios}")
