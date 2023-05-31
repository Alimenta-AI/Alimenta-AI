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
            CNPJ = input('CNPJ (Apenas Números): ')
            if len(CNPJ) == 14:
                return CNPJ
            else:
                print("Error! Quantidade de caracteres incorreta.")
        except ValueError:
            print("Error! Digite valores válidos!")



def clienteID():
    while True:
        try:
            cliente = input("Digite o clienteID: ")
            return cliente
        except ValueError:
            print("Erro! Digite valores válidos!")
            break


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

def confereClienteExistente(clienteId):
    # Executar uma consulta para verificar se o clienteId existe na tabela cliente
    sql = "SELECT COUNT(*) FROM cliente WHERE clienteId = :clienteId"

    # Executar a consulta
    from controller import inst_SQL
    inst_SQL.execute(sql, {'clienteId': clienteId})
    result = inst_SQL.fetchone()

    # Verificar se o clienteId existe
    if result[0] > 0:
        return True
    else:
        return False

def confereInstituicaoExistente(cnpj):
    dados = f"""SELECT * FROM Instituicao WHERE cnpj = '{cnpj}'"""
    from controller import inst_SQL
    inst_SQL.execute(dados)
    listaInstituicao = inst_SQL.fetchall()
    if len(listaInstituicao) != 0:
        return True
    else:
        return False


def endereco():
    while True:
        try:
            enderecoCompleto = input('Endereco: ')
            return enderecoCompleto
        except ValueError:
            print("Erro! Digite valores válidos!")


def website():
    while True:
        try:
            website = input("Digite o website: ")
            return website
        except ValueError:
            print("Erro! Digite valores válidos!")


def tipo():
    while True:
        try:
            tipo = input("Digite o tipo: ")
            return tipo
        except ValueError:
            print("Erro! Digite valores válidos!")

def puxarClienteId():
    try:
        clienteId = input("Digite o clienteId: ")

        # Executar uma consulta para buscar o clienteId na tabela cliente
        sql = "SELECT clienteid FROM Cliente WHERE clienteid = :clienteId"

        # Crie um objeto de cursor para executar a consulta
        from controller import conn
        cursor = conn.cursor()

        # Executar a consulta SQL
        cursor.execute(sql, {'clienteId': clienteId})
        result = cursor.fetchone()

        # Feche o cursor
        cursor.close()

        # Verificar se o clienteId existe
        if result is not None:
            return result[0]  # Retorna o clienteId encontrado na tabela cliente
        else:
            return None  # Retorna None se o clienteId não existir na tabela cliente
    except Exception as erro:
        print("Erro ao buscar clienteId na tabela cliente:", erro)
        return None

