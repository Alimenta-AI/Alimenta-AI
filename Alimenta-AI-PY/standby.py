def subMenuDoacao():
    print(
        '============== <<< ''\033[1;92m''Alimenta-AI''\033[0;0m'' >>> ==============')
    print('|  [''\033[1;32m''1''\033[0;0m''] Tipos de Doacao                       |')
    print('|  [''\033[1;32m''2''\033[0;0m''] Empresas                              |')
    print('|  [''\033[1;32m''0''\033[0;0m''] Voltar                                |')
    print('----------------------------------------------')
    x = input('\033[1;32m''Insira a opção: ''\033[0;0m')
    print('----------------------------------------------')

    if x == '1':
        # Opção selecionada: Tipos de Doacao
        print('Tipos de Doacao')
        print('1. Alimento')
        print('2. Dinheiro')
        tipo_doacao = input('Insira a opção: ')

        print('Tipo de doação selecionado:', tipo_doacao)

        if tipo_doacao == '1':
            print()
            query = "SELECT nome FROM Alimento"
            inst_SQL.execute(query)
            resultados = inst_SQL.fetchall()

            # Exibir os resultados com números sequenciais
            print('\033[1;32mAlimentos Disponíveis\033[0;0m')
            contador = 1
            for row in resultados:
                print(f"{contador}: {row[0]}")
                contador += 1

        '''tipo_doacao == '2':
            print()
            queryDinheiro = "SELECT clienteid FROM Instituicao"
            inst_SQL.execute(queryDinheiro)
            resultado = inst_SQL.fetchall()

            print('\033[1;32mEmpresas Disponíveis Para Doação\033[0;0m32')
            contador = 1
            for row in resultado:
                print(f"{contador}: {row[0]}")
                contador += 1'''

        if tipo_doacao == '2':
            print()
            queryDinheiro = "SELECT clienteid FROM Instituicao"
            inst_SQL.execute(queryDinheiro)
            resultado = inst_SQL.fetchall()

            print('\033[1;32mEmpresas Disponíveis Para Doação\033[0;0m')
            contador = 1
            empresas = []
            for row in resultado:
                empresas.append(row[0])
                print(f"{contador}: {row[0]}")
                contador += 1

            empresa_selecionada = input(
                'Insira o número da empresa para doação: \n')
            if empresa_selecionada.isdigit() and int(empresa_selecionada) <= len(empresas):
                empresa_id = empresas[int(empresa_selecionada) - 1]

                queryEmpresa = f"SELECT * FROM Instituicao WHERE clienteid = '{empresa_id}'"
                try:
                    inst_SQL.execute(queryEmpresa)
                    detalhes_empresa = inst_SQL.fetchone()

                    print('\nDetalhes da Empresa:')
                    print('ID:', detalhes_empresa[0])
                    print('WebSite:', detalhes_empresa[1])
                    print('CNPJ:', detalhes_empresa[2])

                except Exception as e:
                    print('Ocorreu um erro ao obter os detalhes da empresa:', str(e))
            else:
                print('Opção inválida.')

    elif x == '2':

        limpaTerminal()

        print('=== << ''\033[1;33m''Dados da Instituicao''\033[0;0m'' >> ===')

        criaBarra()

        print('\033[1;33m''Lista de Instituicoes Cadastradas:''\033[0;0m')

        criaBarra()

        dados = "SELECT * FROM Instituicao"

        inst_SQL.execute(dados)

        listaInstituicao = inst_SQL.fetchall()

        if len(listaInstituicao) != 0:

            for Instituicao in listaInstituicao:
                print(f'''\033[1;32mClienteID: \033[0;0m{Instituicao[0]}''')

                print(f'''\033[1;32mWebsite: \033[0;0m{Instituicao[1]}''')

                print(f'''\033[1;32mTipo: \033[0;0m{Instituicao[2]}''')

                print(f'''\033[1;32mCnpj: \033[0;0m{Instituicao[3]}''')

                criaBarra()

        else:

            print('\033[1;31m''Nenhuma Instituicao cadastrada!''\033[0;0m')

        subMenuDoacao()
    elif x == '0':
        # Opção selecionada: Voltar
        print('Voltar')

    else:
        # Opção inválida
        print('Opção inválida')

    return x


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
            # Retorna o clienteId encontrado na tabela cliente
            return result[0]
        else:
            return None  # Retorna None se o clienteId não existir na tabela cliente
    except Exception as erro:
        print("Erro ao buscar clienteId na tabela cliente:", erro)
        return None


def confereInstituicaoExistente(cnpj):
    dados = f"""SELECT * FROM Instituicao WHERE cnpj = '{cnpj}'"""
    from controller import inst_SQL
    inst_SQL.execute(dados)
    listaInstituicao = inst_SQL.fetchall()
    if len(listaInstituicao) != 0:
        return True
    else:
        return False


def usuariosCadastrados():
    limpaTerminal()
    print('''\033[1;32m=== Usuarios Cadastrados ===\033[0;0m''')
    # Usuario
    dados = f"""SELECT * FROM usuario"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    for usuario in listaUsuario:
        nome = usuario[0]
        cpf = usuario[1]
        nascimento = usuario[2]
        print(
            f'''\033[1;32mNome: \033[0;0m{nome} | \033[1;32mcpf: \033[0;0m{cpf} | \033[1;32mNascimento: \033[0;0m{nascimento} ''')
    criaBarra()

    return


def relatorio():
    limpaTerminal()
    arquivo = open('relatorio.txt', 'w+')
    arquivo.write('Relatorio de Usuarios \n')
    arquivo.write('\n')

    # Consulta SQL para obter os nomes dos usuários
    dados = """SELECT clienteid FROM usuario"""
    inst_SQL.execute(dados)
    listaNomes = inst_SQL.fetchall()

    countUsers = len(listaNomes)
    arquivo.write(f'A Alimenta-AI possui {countUsers} usuarios \n')
    for i, nome in enumerate(listaNomes, start=1):
        arquivo.write(f'{i}.{nome[0]} \n')
    arquivo.write(f'{dia}/{mes}/{ano}')
    criaBarra()
    print('\033[1;32m'"Relatorio gerado em 'relatorio.txt'"'\033[0;0m')
    criaBarra()
    arquivo.close()
    return
