

def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    print("Contato adicionado/atualizado com sucesso!")


def buscar_telefone(agenda, nome):
    if nome in agenda:
        return agenda[nome]
    else:
        return "Contato não encontrado."


def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        return "Contato removido com sucesso."
    else:
        return "Contato não encontrado."


def listar_contatos(agenda):
    if not agenda:
        print("Agenda vazia.")
    else:
        print("\nLista de contatos:")
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")




agenda = {}

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar contato")
    print("2 - Buscar telefone")
    print("3 - Remover contato")
    print("4 - Listar contatos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        adicionar_contato(agenda, nome, telefone)

    elif opcao == "2":
        nome = input("Nome do contato: ")
        print(buscar_telefone(agenda, nome))

    elif opcao == "3":
        nome = input("Nome do contato: ")
        print(remover_contato(agenda, nome))

    elif opcao == "4":
        listar_contatos(agenda)

    elif opcao == "5":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")