import json

try:
    with open("clientes.json", "r") as f:
        clientes = json.load(f)
except:
    clientes = []

def salvar():
    with open("clientes.json", "w") as f:
        json.dump(clientes, f)

def menu():
    print("1 - Cadastrar")
    print("2 - Buscar")
    print("3 - Alterar")
    print("4 - Apagar")
    print("5 - Mostrar todos")
    print("6 - Sair")
    opt = int(input("O que você quer fazer?: "))
    return opt

def cadastrar():
    cliente = {}

    cliente["nome"] = str(input("Digite o nome: "))
    cliente["cpf"] = str(input("Digite o CPF: "))
    cliente["tel"] = str(input("Digite o telefone: "))
    cliente["email"] = str(input("Digite o E-Mail: "))
    cliente["end"] = str(input("Digite o endereço: "))
    clientes.append(cliente)
    salvar()

def buscar():
    id = str(input("Digite o CPF do cliente: "))
    for cliente in clientes:
        if id == cliente["cpf"]:
            print(f"Nome: {cliente["nome"]}")
            print(f"CPF: {cliente["cpf"]}")
            print(f"Telefone: {cliente["tel"]}")
            print(f"E-mail: {cliente["email"]}")
            print(f"Endereço: {cliente["end"]}")
            break
    else:
        print("Cliente não encontrado!")

def alterar():
    id = str(input("Digite o CPF do cliente: "))
    for cliente in clientes:
        if id == cliente["cpf"]:
            cf = input(f"Tem certeza que quer alterar os dados do cliente {cliente['cpf']}? (y/n): ")
            if cf.upper() == "Y":
                cliente["nome"] = str(input("Digite o nome: "))
                cliente["cpf"] = str(input("Digite o CPF: "))
                cliente["tel"] = str(input("Digite o telefone: "))
                cliente["email"] = str(input("Digite o E-Mail: "))
                cliente["end"] = str(input("Digite o endereço: "))
                salvar()
                break
            else:
                print("Operação cancelada!")
    else:
        print("Cliente não encontrado!")

def apagar():
    id = str(input("Digite o CPF do cliente: "))
    for cliente in clientes:
        if id == cliente["cpf"]:
            cf = input(f"Tem certeza que quer apagar {cliente['cpf']}? (y/n): ")
            if cf.upper() == "Y":
                clientes.remove(cliente)
                salvar()
                break
            else:
                print("Operação cancelada!")
    else:
        print("Cliente não encontrado!")

def mt():
    for cliente in clientes:
        print(f"Nome: {cliente["nome"]}")
        print(f"CPF: {cliente["cpf"]}")
        print(f"Telefone: {cliente["tel"]}")
        print(f"E-mail: {cliente["email"]}")
        print(f"Endereço: {cliente["end"]}")

while True:

    opt = menu()

    if opt == 1:
        cadastrar()
    elif opt == 2:
        buscar()
    elif opt == 3:
        alterar()
    elif opt == 4:
        apagar()
    elif opt == 5:
        mt()
    elif opt == 6:
        print("Programa encerrado!")
        break