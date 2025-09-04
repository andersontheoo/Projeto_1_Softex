'''Projeto 1 – Sistema de Gerenciamento de Alunos'''

alunos= []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    while True:
        try:
            nota = float(input("Digite a nota do aluno (0 a 10): "))
            if 0 <= nota <= 10:
                nota = round(nota, 1)  
                break  
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Por favor, insira um valor válido para a nota.")

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota,  
    }

    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!\n")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado. Cadastre primeiro!\n")
        return
    print("\n--- Lista de Alunos ---")
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. Nome: {aluno['nome']} --- Idade: {aluno['idade']} --- Nota: {aluno['nota']}")
    print()


def buscar_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado ainda.\n")
        return
    
    nome_busca = input("Digite o nome do aluno que deseja buscar: ").strip().lower()
    encontrados = []

    for aluno in alunos:
        # Comparação que busca por parte do nome (melhoria)
        if nome_busca in aluno["nome"].lower():
            encontrados.append(aluno)

    if encontrados:
        print("\n--- Alunos encontrados ---")
        for i, aluno in enumerate(encontrados, start=1):
            print(f"{i}. Nome: {aluno['nome']} --- Idade: {aluno['idade']} --- Nota: {aluno['nota']}")
    else:
        print(f"Nenhum aluno com o nome '{nome_busca}' foi encontrado.\n")

while True:
    print("*****===== MENU =====*****")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos cadastrados")
    print("3 - Buscar aluno pelo nome")
    print("4 - Listar aprovados e reprovados")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if not opcao.isdigit():  # garante que é um número
        print("Digite apenas números de 1 a 5.\n")
        continue

    opcao = int(opcao)

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        listar_alunos()
    elif opcao == 3:
        buscar_aluno()
    elif opcao == 4:
        print("listar_aprovados_reprovados()")
    elif opcao == 5:
        print("Programa finalizado!")
        break
    else:
        print("Opção inválida! Escolha um número entre 1 e 5.\n")

