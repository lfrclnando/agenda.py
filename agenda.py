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

# Edit contact
def edit_contact(agenda, indice_contact, new_name, new_phone, new_email, new_favorite):
    new_indice_contact = int(indice_contact) - 1
    if new_indice_contact in range(len(agenda)):
        contact, info = agenda[new_indice_contact]
        if new_name.strip():
            info["nome"] = new_name
        if new_phone.strip():
            info["telefone"] = new_phone
        if new_email.strip():
            info["e-mail"] = new_email
        if new_favorite.strip():
            info["favorito"] = format_favorite(new_favorite)
        print(f"Contato '{info['nome']}' editado com sucesso!")
    else:
        print("Contato não encontrado!")

# Formatting favorites
def format_favorite(value):
    if value.lower() in ('sim', 's'):
        return "Sim"
    elif value.lower() in ('não', 'n'):
        return "Não"
    return

# Edit favorite
def toggle_favorite(agenda, indice_contact):
    if 0 < indice_contact <= len(agenda):
        contact, info = agenda[indice_contact - 1]
        info["favorito"] = "Sim" if info["favorito"] == "Não" else "Não"
        print(f"Contato '{info['nome']}' marcado como favorito: {info['favorito']}")
    else:
        print("Contato não encontrado!")
    return

# See favorites contacts
def see_favorite_contacts(agenda, indice_contact):
    for indice_contact, (contact, info) in enumerate(agenda, start=1):
        if info["favorito"] == "Sim":
            print(f"{indice_contact}. {info['nome']} - {info['telefone']} - {info['e-mail']} - Favorito: {info['favorito']}")
    return

agenda = []
while True:
    print("\nBEM VINDO(A) À SUA AGENDA!!!\n")
    print("1. Adicionar um novo contato")
    print("2. Ver um contato")
    print("3. Ver uma lista de todos os contatos")
    print("4. Editar um contato")
    print("5. Marcar/Desmarcar um contato como favorito")
    print("6. Ver uma lista dos contatos favoritos")
    print("7. Apagar um contato")
    print("8. Sair")

    desire = int(input("\nDigite um número de 1 ao 9 para escolher: "))
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
    elif desire == 4:
        see_contacts(agenda)
        indice_contact = int(input("Digite o número do contato a ser alterado: "))
        new_name = input("Digite o novo nome (ou deixe em branco para manter o atual): ")
        new_phone = input("Digite o novo telefone (ou deixe em branco para manter o atual): ")
        new_email = input("Digite o novo e-mail (ou deixe em branco para manter o atual): ")
        new_favorite = input("O contato é favorito? Sim ou Não (ou deixe em branco para manter o atual): ")
        edit_contact(agenda, indice_contact, new_name.capitalize(), new_phone, new_email, new_favorite.capitalize())
    elif desire == 5:
        indice_contact = int(input("Digite o número do contato: "))
        toggle_favorite(agenda, indice_contact)
    elif desire == 6:
        see_favorite_contacts(agenda, indice_contact)
    

    elif desire == 8:
        break
print("Programa Finalizado...")
       