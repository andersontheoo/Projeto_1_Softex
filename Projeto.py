'''Projeto 1 – Sistema de Gerenciamento de Alunos'''

alunos= []
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))

    alunos = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

for i in range(5):
    print(f"\n -- Cadastro do Aluno {i+1} de 5 ---")
    cadastrar_aluno()

print("\n Lista de alunos:")
for i, aluno in enumerate(alunos, 1):
    print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")

# alunos = []

# def cadastrar_aluno():
#     nome = input("Digite o nome do aluno: ")
#     idade = int(input("Digite a idade do aluno: "))
#     nota = float(input("Digite a nota do aluno: "))

#     aluno = {
#         "nome": nome,
#         "idade": idade,
#         "nota": nota
#     }

#     alunos.append(aluno)
#     print(f"✅ Aluno {nome} cadastrado com sucesso!\n")

# # Loop para cadastrar até 10 alunos
# for i in range(10):
#     print(f"\n--- Cadastro do aluno {i+1} de 10 ---")
#     cadastrar_aluno()

# print("\n📋 Lista final de alunos:")
# for i, aluno in enumerate(alunos, 1):
#     print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")
