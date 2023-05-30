from prettytable import PrettyTable
import random


def Nome():
    while True:
        nome = input('Nome Completo: ')
        if nome == '':
            print('Error! Entrada vazia.')
            continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                break
        else:
            return nome.strip(' ')


def Senha():
    while True:
        senha = input('Senha: ')
        if senha == '':
            print('Error! Entrada vazia.')
            continue
        return senha.strip(' ')


def Email():
    while True:
        email = input('Email: ')
        if email == '':
            print('Error! Entrada vazia.')
        elif '@' and '.com' in email:
            return email.strip(' ')
        else:
            print('Email Inválido! Deve conter "@" e ".com"')


def Celular():
    while True:
        celular = input('Celular (Apenas Números): ')
        if celular == '':
            print('Error! Entrada vazia.')
            continue
        elif not celular.isnumeric():
            print('Insira apenas números.')
            continue
        else:
            if 9 <= len(celular) <= 11:
                return celular
            else:
                print('O número deve ter entre 9 - 11 dígitos.')


def Data():
    while True:
        data = input('Nascimento (dd/mm/aaaa): ')
        if data == '':
            print('Error! Entrada vazia.')
            continue
        temp = ''.join(data.split('/'))  # Retorna string de valores sem '/'
        if not temp.isnumeric():  # Analisa se string tem caracteres
            print('Insira uma data válida')
            continue
        # Retorna o número de '/' na data
        if data.count('/') == 2 and data != '//':
            dia, mes, ano = data.split('/')
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2022:
                print(data.strip(' '))
                return data.strip(' ')
            else:
                print('Dia/Mes/Ano Inválido(s)')
        else:
            print('A data deve seguir o padrão dd/mm/aaa')


def Cpf():
    while True:
        try:
            cpf = input('CPF (Apenas Números): ')
            if len(cpf) == 11:
                return cpf
            else:
                print("Error! Quantidade de caracteres incorreta.")
        except ValueError:
            print("Error! Digite valores válidos!")


def cnpj():
    while True:
        try:
            CNPJ = input(int('CNPJ (Apenas Números): '))
            if len(CNPJ) == 14:
                return CNPJ
            else:
                print("Error! Quantidade de caracteres incorreta.")
        except ValueError:
            print("Error! Digite valores válidos!")


def clienteID():
    return None


def tipo_cliente():
    while True:
        try:
            tipo = int(
                input('Tipo de Cliente (0 - Pessoa Física, 1 - Pessoa Jurídica): '))
            if tipo == 0 or tipo == 1:
                return tipo
            else:
                print("Erro! Digite um valor válido (0 ou 1).")
        except ValueError:
            print("Erro! Digite um valor válido (0 ou 1).")


def endereco():
    while True:
        try:
            cep = input('CEP: ')
            endereco = input('Endereco: ')
            numero = input('Número: ')
            cidade = input('Cidade: ')
            estado = input('Estado: ')

            enderecoCompleto = ', '.join(
                [cep, endereco, numero, cidade, estado])

            return enderecoCompleto
        except ValueError:
            print("Erro! Digite valores válidos!")


def tipo():
    return None


def website():
    return None