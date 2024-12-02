from funcoes_parte_inicial import *
from funcoes_parte_central import *


nome_aluno = str(input("Digite o nome do Aluno: "))
idade_aluno = int(input("Digite a idade do Aluno: "))
cronograma_treinos_academia()
treinos = lista_exercicios

academia = {
    "Dados do Aluno": {
        "nome": nome_aluno,
        "Idade": idade_aluno,
        "Treino": [
            {"data": "2024/Dezembro", "exercicios": [lista_exercicios]}
        ]
    }
}

print(academia)

