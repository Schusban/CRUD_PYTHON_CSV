import csv
import os

csvFilename = 'data_contact.csv'
csv_filename = 'cursos_email.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print(f'''================ ALUNOS ================
[1] Visualizar aluno
[2] Cadastrar aluno
[3] Editar aluno
[4] Deletar cadastro de aluno
[5] Procurar aluno
[0] Sair
=======================================''')
    selected_menu = input("Escolha uma alternativa => ")

    if(selected_menu == "1"):
        mostrar_aluno()
    elif(selected_menu == "2"):
        criar_aluno()
    elif(selected_menu == "3"):
        editar_contato()
    elif(selected_menu == "4"):
        deletar_aluno()
    elif(selected_menu == "5"):
        consultar_aluno()
    elif(selected_menu == "0"):
        exit()
    else:
        print("ALTERNATIVA INVALIDA!!!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Pressione ENTER para voltar")
    show_menu()

def mostrar_aluno():
    clear_screen()
    contacts = []
    with open(csvFilename, mode="r") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=",")
        for row in csvReader:
            contacts.append(row)

    if (len(contacts) > 0):

        print("MATRICULA \t NOME \t CELULAR")
        print("-" * 34)
        for data in contacts:
            print(f"{data['MATRICULA']} \t {data['NOME']} \t {data['CELULAR']}".format(*row))
    else:
      print("DADO NAO ENCONTRADO")

    back_to_menu()

def criar_aluno():
    clear_screen()
    with open(csvFilename, mode='a') as csvFile:
        fieldNames = ['MATRICULA', 'NOME', 'CELULAR']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

        matricula = input("Matricula : ")
        nome = input("Nome Completo : ")
        celular = input("Numero de telefone : ")

        writer.writerow({'MATRICULA' : matricula, 'NOME': nome, 'CELULAR': celular})
        print("Succes")

    back_to_menu()
def editar_contato():
    clear_screen()
    contacts = []

    with open(csvFilename, mode="r") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            contacts.append(row)

    print(f'''MATRICULA \t NOME \t CELULAR")
*34''')

    for data in contacts:
        print(f"{data['MATRICULA']} \t {data['NOME']} \t {data['CELULAR']}")

    print("-"*12)
    matricula = input("MATRICULA : ")
    nome = input("Novo nome : ")
    celular = input("Novo numero : ")

    indeks = 0
    for data in contacts:
        if(data['MATRICULA'] == matricula):
            contacts[indeks]['NOME'] = nome
            contacts[indeks]['CELULAR'] = celular
        indeks = indeks + 1

    with open(csvFilename, mode="w") as csvFile:
        fieldNames = ['MATRICULA', 'NOME', 'CELULAR']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()
        for newData in contacts:
            writer.writerow({'MATRICULA': newData['MATRICULA'],'NOME': newData['NOME'] ,'CELULAR': newData['CELULAR'] })

    back_to_menu()

def deletar_aluno():
    clear_screen()
    contacts = []

    with open(csvFilename, mode="r") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            contacts.append(row)

    print(f'''MATRICULA \t NOME COMPLETO \t CELULAR
*32''')

    for data in contacts:
        print(f"{data['MATRICULA']} \t {data['NOME']} \t {data['CELULAR']}")

    print("-"*12)
    matricula = input("Delete MATRICULA :")

    indeks = 0
    for data in contacts:
        if (data['MATRICULA'] == matricula):
            contacts.remove(contacts[indeks])
        indeks = indeks + 1

    with open(csvFilename, mode="w") as csvFile:
        fieldNames = ['MATRICULA', 'NOME', 'CELULAR']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()
        for newData in contacts:
            writer.writerow({'MATRICULA': newData['MATRICULA'], 'NOME': newData['NOME'], 'CELULAR': newData['CELULAR']})

    print("DADOS DELETADOS!!")
    back_to_menu()

def consultar_aluno():
    clear_screen()
    contacts = []

    with open(csvFilename, mode="r") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            contacts.append(row)

    matricula = input("Procurar pela matricula > ")

    data_found = []

    #search data contact
    indeks = 0
    for data in contacts:
        if(data['MATRICULA'] == matricula):
            data_found = contacts[indeks]

        indeks = indeks + 1

    if len(data_found) > 0:
        print(f'''DADOS ENCONTRADOS : 
        Nome: {data_found['NOME']}
        Celular: {data_found['CELULAR']}''')
    else:
        print("DADOS NAO ENCONTRADOS")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()