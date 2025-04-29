import json
import os

ARQUIVO = "contatos.json"

def carregar_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_contatos(contatos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=4, ensure_ascii=False)

contatos = carregar_contatos()

def adicionar_contato(): 
    nome = input("Digite o nome do contato: ") 
    telefone = input("Digite o telefone do contato: ") 
    contatos.append({"nome": nome, "telefone": telefone})
    salvar_contatos(contatos)
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    if not contatos:
        print("Nenhum contato encontrado.")
    else:
        print("Lista de Contatos:")
        for indice, contato in enumerate(contatos):
            print(f"{indice}: {contato['nome']} - {contato['telefone']}")

def buscar_contato():
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    nome = input("Digite o nome do contato que deseja buscar: ")
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            print(f"Contato encontrado: {contato['nome']} - {contato['telefone']}")
            return
    print("Contato não encontrado.")

def editar_contato():
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    nome = input("Digite o nome do contato que deseja editar: ")   
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")
            contato["nome"] = novo_nome
            contato["telefone"] = novo_telefone
            salvar_contatos(contatos)
            print(f"Contato {nome} editado com sucesso!")
            return 
    print("Contato não encontrado.")

def excluir_contato():
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    nome = input("Digite o nome do contato que deseja excluir: ")
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            contatos.remove(contato)
            salvar_contatos(contatos)
            print(f"Contato {nome} excluído com sucesso!")
            return
    print("Contato não encontrado.")

def menu():
    while True:
        print("""
            === Agenda de Contatos ===
                1. Adicionar
                2. Listar
                3. Buscar
                4. Editar
                5. Excluir
                6. Sair
                """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            editar_contato()
        elif opcao == "5":
            excluir_contato()
        elif opcao == "6":
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
