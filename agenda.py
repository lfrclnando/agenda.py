# Adding contacts
def add_contact(agenda, name, phone, email, favorite):
    contact = ("contato", {"nome": name, "telefone": phone, "e-mail": email, "favorito": favorite})
    agenda.append(contact)
    print(f"Foi adicionado com sucesso o contato:\n'{name}'; \ntelefone '{phone}'; \ne-mail '{email}'; \nEstá marcado como favorito? '{favorite}'")
    return

# See one contact
def see_one_contact(agenda):
    indice = int(input("Digite o número do contato: "))
    if 0 < indice <= len(agenda):
        contact, info = agenda[indice - 1]
        print(f"{info['nome']} - {info['telefone']} - {info['e-mail']} - Favorito: {info['favorito']}")
    else:
        print("Registro não encontrado!")
    return

# See contacts
def see_contacts(agenda):
    for indice, (contact, info) in enumerate(agenda, start=1):
        print(f"{indice}. {info['nome']} - {info['telefone']} - {info['e-mail']} - Favorito: {info['favorito']}")
    return

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
        favorite = input("O contato é favorito? Sim ou Não: ")
        add_contact(agenda, name.capitalize(), phone, email, favorite.capitalize())
    elif desire == 2:
        see_one_contact(agenda)
    elif desire == 3:
        see_contacts(agenda)
    elif desire == 9:
        break
print("Programa Finalizado...")
       