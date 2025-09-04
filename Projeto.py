'''Projeto 1 – Sistema de Gerenciamento de Alunos'''
'''Projeto 1 – Sistema de Gerenciamento de Alunos'''

alunos= []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno (0 a 10): "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": round(nota, 1)  # garante 1 casa decimal
    }

    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!\n")

def listar_aprovados_reprovados():
    if not alunos:
        print("Nenhum aluno cadastrado. Cadastre primeiro!\n")
        return
    media= sum(aluno["nota"] for aluno in alunos) / len(alunos)
   
    print(f"\n media da turma {media:.2f} \n:")

    aprovados = [aluno["nome"] for aluno in alunos if aluno["nota"] <= 7]
    reprovados = [aluno["nome"] for aluno in alunos if aluno["nota"] >7]

    print("aprovados")
    if aprovados:
        for nome in aprovados:
            print(f"{nome}")
    else:
        print("nenhum aluno aprovados")
    
    print("\n reprovados")
    if reprovados:
        for nome in reprovados:
            print(f"{nome}")
    else:
            print("nenhum aluno reprovado") 
    print()  

while True:
    print("*****===== MENU =====*****") 
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos cadastrados")
    print("3 - Buscar aluno pelo nome")
    print("4 - Listar aprovados e reprovados")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if not opcao.isdigit():  # garante que é um número
        print("⚠ Digite apenas números de 1 a 5.\n")
        continue

    opcao = int(opcao)

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        print("listar_alunos()")
    elif opcao == 3:
        print("buscar_aluno()")
    elif opcao == 4:
        listar_aprovados_reprovados()
    elif opcao == 5:
        print("Programa finalizado!")
        break
    else:
        print("Opção inválida! Escolha um número entre 1 e 5.\n")



