
agenda = []
while True:
    print("\nO que deseja fazer em sua agenda?")
    print("1. Adicionar um novo contato")
    print("2. Ver um contato")
    print("3. Ver uma lista de todos os contatos")
    print("4. Editar um contato")
    print("5. Marcar/Desmarcar um contato como favorito")
    print("6. Ver um contato favorito")
    print("7. Ver uma lista dos contatos favoritos")
    print("8. Apagar um contato")
    print("9. Sair")

    desire = int(input("Digite seu desejo: "))
    if desire == 1:
        name = input("Digite o nome: ")
        phone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")
        favorite = input("Digite sim se o contato for favorito: ")
        contact = {"name": name, "phone": phone, "email": email, "favorite": favorite}
        agenda.append(contact)
        print("Contato adicionando com sucesso!")
        
    elif desire == 9:
        break
    print("Programa Finalizado...")
       