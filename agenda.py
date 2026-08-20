contatos = []


def cadastrar_contato():
    pass


def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    for indice, contato in enumerate(contatos, start=1):
        print(
            f"{indice}. {contato['nome']} - {contato['telefone']} "
            f"({contato['email']})"
        )


def buscar_contato():
    pass


def remover_contato():
    pass


while True:
    print("\n=== Agenda de Contatos ===")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair")
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        print("Ate logo!")
        break
    else:
        print("Opcao invalida.")
