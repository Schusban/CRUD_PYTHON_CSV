import csv
import os
# import threading

matriculacsv = 'data_contact.csv'
cursoEmail = 'cursos_email.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print(f'''================ ALUNOS ================
[1] Cadastrar aluno
[2] Editar aluno
[3] Deletar cadastro de aluno
[4] Procurar aluno
[5] Registrar curso e e-mail
[6] Editar curso e e-mail
[0] Sair
=======================================''')
    selected_menu = input("Escolha uma alternativa => ")

    if selected_menu == "1":
        return criar_aluno()
    elif selected_menu == "2" :
        return editar_contato()
    elif selected_menu == "3":
        return deletar_aluno(), deletar_info()
    elif selected_menu == "4":
        return consultar_aluno()
    elif selected_menu == "5":
        return registrar_info()
    elif selected_menu == "6":
        return editar_info()
    elif selected_menu == "0":
        return exit()
    else:
        print("ALTERNATIVA INVALIDA!!!")

def back_to_menu():
    input("\nPressione ENTER para voltar")
    show_menu()

def criar_aluno():
    clear_screen()
    with open(matriculacsv, mode='a', newline="") as csvFile:
        fieldNames = ['MATRICULA', 'NOME', 'CELULAR']
        # writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        matriculainput = input("Matricula : ")
        nome = input("Nome Completo : ")
        celular = input("Numero de telefone : ")
        writer.writerow({'MATRICULA' : matriculainput, 'NOME': nome, 'CELULAR': celular})
        print("Aluno cadastrado")

def registrar_info():
    clear_screen()
    with open(cursoEmail, mode='a', newline="") as csvFile:
        fieldNames = ['MATRICULA', 'CURSO', 'EMAIL']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        matricula = input("Matricula : ")
        curso = input("Curso : ")
        email = input("E-MAIL : ")
        writer.writerow({'MATRICULA' : matricula, 'CURSO' : curso, 'EMAIL': email})
        print("Informações cadastradas")

def editar_contato():
    clear_screen()
    contacts = []
    with open(matriculacsv, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    print(f'MATRICULA \t\t NOME \t\t CELULAR')
    for data in contacts:
        print(f'''{data['MATRICULA']} \t\t {data['NOME']} \t\t {data['CELULAR']}''')
    matricula = input("MATRICULA : ")
    nome = input("Novo nome : ")
    celular = input("Novo numero : ")
    index = 0
    for data in contacts:
        if data['MATRICULA'] == matricula:
            contacts[index]['NOME'] = nome
            contacts[index]['CELULAR'] = celular
        index = index + 1
    with open(matriculacsv, mode="w", newline="") as csvFile:
        fieldNames = ['MATRICULA', 'NOME', 'CELULAR']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer.writeheader()
        for newData in contacts:
            writer.writerow({'MATRICULA': newData['MATRICULA'],'NOME': newData['NOME'] ,'CELULAR': newData['CELULAR'] })

def editar_info():
    clear_screen()
    contacts = []
    with open(cursoEmail, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    print(f'MATRICULA \tCURSO \t EMAIL')
    for data in contacts:
        print(f"{data['MATRICULA']} \t {data['CURSO']} \t {data['EMAIL']}")
    print("-"*12)
    matri = input("ID do aluno : ")
    curso = input("Curso atual : ")
    email = input("Novo e-mail : ")
    index = 0
    for data in contacts:
        if data['MATRICULA'] == matri:
            contacts[index]['CURSO'] = curso
            contacts[index]['EMAIL'] = email
        index = index + 1
    with open(cursoEmail, mode="w", newline="") as csvFile:
        fieldNames = ['MATRICULA', 'CURSO', 'EMAIL']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer.writeheader()
        for newData in contacts:
            writer.writerow({'MATRICULA': newData['MATRICULA'], 'CURSO': newData['CURSO'], 'EMAIL': newData['EMAIL']})

def deletar_aluno():
    global matriculadel
    contacts = []
    with open(matriculacsv, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    print(f'MATRICULA \t NOME COMPLETO \t CELULAR')
    for data in contacts:
        print(f"{data['MATRICULA']} \t {data['NOME']} \t {data['CELULAR']}")
    print("-"*12)
    matriculadel = input("Delete MATRICULA :")
    index = 0
    for data in contacts:
        if data['MATRICULA'] == matriculadel:
            contacts.remove(contacts[index])
        index = index + 1
    with open(matriculacsv, mode="w", newline="") as csvFile:
        fieldNames = ['MATRICULA', 'NOME', 'CELULAR']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer.writeheader()
        for newData in contacts:
            writer.writerow({'MATRICULA': newData['MATRICULA'], 'NOME': newData['NOME'], 'CELULAR': newData['CELULAR']})

def deletar_info():
    clear_screen()
    contacts = []
    with open (cursoEmail, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    print(f'CURSO \t E-MAIL')
    for data in contacts:
        print(f"{data['CURSO']} \t {data['EMAIL']}")
    index = 0
    for data in contacts:
        if data['MATRICULA'] == matriculadel:
            contacts.remove(contacts[index])
        index = index + 1
    with open(cursoEmail, mode="w", newline="") as csvFile:
        fieldNames = ['MATRICULA', 'CURSO', 'EMAIL']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer.writeheader()
        for newData in contacts:
            writer.writerow({'MATRICULA': newData['MATRICULA'],'CURSO': newData['CURSO'], 'EMAIL': newData['EMAIL']})

def consultar_aluno():
    clear_screen()
    contacts = []
    with open(matriculacsv, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    emails = []
    email_found = []
    with open(cursoEmail, mode="r", newline="") as csvemail:
        csvReader = csv.DictReader(csvemail, delimiter=',')
        for row2 in csvReader:
            emails.append(row2)
    matriculab = input("Procurar pela matricula > ")
    data_found = []
    index = 0
    index2 = 0
    for data in contacts:
        if data['MATRICULA'] == matriculab:
            data_found = contacts[index]
        index = index + 1
    for j in emails:
        if j['MATRICULA'] == matriculab:
            email_found = emails[index2]
        index2 = index2 + 1
    print(f'''DADOS ENCONTRADOS: 
Nome: {data_found['NOME']}
Celular: {data_found['CELULAR']}
Curso: {email_found['CURSO']} 
Email: {email_found['EMAIL']}''')


if __name__ == "__main__":
    #while True:
    show_menu()

def registrar_info():
    clear_screen()
    with open(cursoEmail, mode='a', newline="") as csvFile:
        fieldNames = ['MATRICULA', 'CURSO', 'EMAIL']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        matriculai = input("Matrícula : ")
        curso = input("Curso : ")
        email = input("E-mail : ")
        writer.writerow({'MATRICULA' : matriculai, 'CURSO' : curso, 'EMAIL': email})
        print("Informações cadastradas")
