import oracledb
import sys
import service
import datetime
import os
from time import sleep

try:
    dnStr = oracledb.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = oracledb.connect(user='Rm97121', password='290603', dsn=dnStr)
    inst_SQL = conn.cursor()
except Exception as e:
    print("Erro: ", e)
    conexao = False
    inst_SQL = ""
    conn = ""
else:
    conexao = True


def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def criaBarra():
    return print('-' * 32)


data = datetime.datetime.now()
dia = data.day
mes = data.month
ano = data.year


def menuInicial():
    print('=============== <<< ''\033[1;92m''Alimenta-AI''\033[0;0m'' >>> ===============')
    print('|  [''\033[1;32m''1''\033[0;0m''] Clientes                                 |')
    print('|  [''\033[1;32m''2''\033[0;0m''] Instituições                             |')
    print('|  [''\033[1;32m''3''\033[0;0m''] Doação                                   |')
    print('|  [''\033[1;32m''0''\033[0;0m''] Sair                                     |')
    print('------------------------------------------------')
    try:
        escolha = int(input('\033[1;32m''Insira a opção: ''\033[0;0m'))
    except ValueError:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuInicial()
        return
    print('------------------------------------------------')

    if escolha == 1:
        limpaTerminal()
        subMenuClientes()
    elif escolha == 2:
        limpaTerminal()
        subMenuInstituicoes()
    elif escolha == 3:
        limpaTerminal()
        subMenuDoacao()
    elif escolha == 0:
        print('\033[1;32m''Fechando administração...''\033[0;0m')
        conn.close()
        sleep(3)
        sys.exit()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuInicial()



def subMenuClientes():
    print(
        '========== <<< ''\033[1;92m''Alimenta-AI''\033[0;0m'' >>> ==========')
    print(
        '|  [''\033[1;32m''1''\033[0;0m''] Cadastrar Usuário              |')
    print(
        '|  [''\033[1;32m''2''\033[0;0m''] Dados do Usuário               |')
    print(
        '|  [''\033[1;32m''3''\033[0;0m''] Mostrar Usuários               |')

    print(
        '|  [''\033[1;32m''4''\033[0;0m''] Gerar Relatório de Usuarios    |')

    print(
        '|  [''\033[1;32m''5''\033[0;0m''] Remover Usuário                |')

    print(
        '|  [''\033[1;32m''0''\033[0;0m''] Voltar                         |')
    print('--------------------------------------')
    try:
        escolha = int(input('\033[1;32m''Insira a opção: ''\033[0;0m'))
    except ValueError:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        subMenuClientes()
        return
    print('--------------------------------------')
    if escolha == 1:
        if (conexao == True):
            cadastro()
            subMenuClientes()
        else:
            print('\033[1;31m''Database was not connect!''\033[0;0m')
    elif escolha == 2:
        mostraDados()
        subMenuClientes()
    elif escolha == 3:
        usuariosCadastrados()
        subMenuClientes()
    elif escolha == 4:
        relatorio()
        subMenuClientes()
    elif escolha == 5:
        removerUsuario()
        subMenuClientes()
    elif escolha == 0:
        sleep(1)
        limpaTerminal()
        menuInicial()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        subMenuClientes()


def subMenuInstituicoes():
    print(
        '========== <<< ''\033[1;92m''Alimenta-AI''\033[0;0m'' >>> ==========')
    print('|  [''\033[1;32m''1''\033[0;0m''] Cadastrar Instituicao               |')
    print('|  [''\033[1;32m''2''\033[0;0m''] Dados do Instituicao                |')
    print('|  [''\033[1;32m''3''\033[0;0m''] Mostrar Instituicoes                |')
    print('|  [''\033[1;32m''4''\033[0;0m''] Gerar Relatorio de Instituicoes     |')
    print('|  [''\033[1;32m''5''\033[0;0m''] Gerenciar Instituicao               |')
    print('|  [''\033[1;32m''6''\033[0;0m''] Remover Instituicao                 |')
    print('|  [''\033[1;32m''0''\033[0;0m''] Voltar                        |')
    print('--------------------------------------')
    try:
        escolha = int(input('\033[1;32m''Insira a opção: ''\033[0;0m'))
    except ValueError:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        subMenuInstituicoes()
        return
    print('--------------------------------------')
    if escolha == 1:
        cadastroInstituicao()
        subMenuInstituicoes()
    elif escolha == 2:
        dadosInstituicao()
        subMenuInstituicoes()
    elif escolha == 3:
        mostrarInstituicao()
        subMenuInstituicoes()
    elif escolha == 4:
        relatorioInstituicao()
        subMenuInstituicoes()
    elif escolha == 5:
        gerenciarInstituicao()
        subMenuInstituicoes()
    elif escolha == 6:
        removeInstituicao()
        subMenuInstituicoes()
    elif escolha == 0:
        sleep(1)
        limpaTerminal()
        menuInicial()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        subMenuInstituicoes()


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

            empresa_selecionada = input('Insira o número da empresa para doação: \n')
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

        print('=== << ''\033[1;33m''Dados do Instituicao''\033[0;0m'' >> ===')

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


''' Função de Cadastrar / Checar login existente / Adicionar dados no arquivo txt de logins '''


def confereLoginExistente(cpf):
    dados = f"""SELECT * FROM usuario WHERE cpf = '{cpf}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    if len(listaUsuario) != 0:
        return True
    else:
        return False

def cadastro():
    try:
        limpaTerminal()
        print('====== < Cadastrar Usuário > ======')

        # Retornando valores validados
        clienteId = service.clienteID()
        nome = service.Nome()
        email = service.Email()
        senha = service.Senha()
        celular = service.Celular()
        endereco = service.endereco()
        cpf = service.Cpf()
        tipoCliente = service.tipo_cliente()

        if confereLoginExistente(cpf):
            print('\033[1;31mLogin já existente!\033[0;0m')
            criaBarra()
            return

        nascimento = ''.join(service.Data().split('/'))
        print(nascimento)

        # Executa o insert na tabela do SQL
        # Executa o insert na tabela do SQL
        cadastroCliente = f"INSERT INTO cliente (clienteId, nome, email, senha, celular, endereco, tipoCliente) VALUES ('{clienteId}', '{nome}', '{email}', '{senha}', '{celular}', '{endereco}', {tipoCliente})"
        cadastroUsuario = f"INSERT INTO usuario (clienteId, cpf, nascimento) VALUES ('{clienteId}', '{cpf}', '{nascimento}')"

        try:
            inst_SQL.execute(cadastroCliente)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Erro ao cadastrar cliente: {e}")

        try:
            inst_SQL.execute(cadastroUsuario)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Erro ao cadastrar usuário: {e}")

        limpaTerminal()
        criaBarra()
        print('\033[1;32mUsuário cadastrado com sucesso!\033[0;0m')
        criaBarra()
    except ValueError:
        print("Digite valores numéricos")
    except Exception as e:
        print(f"Erro de transação com o BD: {e}")


def mostraDados():
    limpaTerminal()
    print('=== << ''\033[1;33m''Dados do Usuario''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Logue para acessar seus dados!''\033[0;0m')
    criaBarra()
    userLogin = input('Login: ')
    userSenha = input('Senha: ')

    # Variavel de validação do login
    valida = False

    dados = f"""SELECT * FROM cliente WHERE clienteid = '{userLogin}' AND senha = '{userSenha}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    if (len(listaUsuario) != 0):
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Usuario Logado! Dados do usuário: ''\033[0;0m')
        criaBarra()
        # Dados do usuario
        for usuario in listaUsuario:
            print(f'''\033[1;32mClienteID: \033[0;0m{usuario[0]}''')
            print(f'''\033[1;32mNome: \033[0;0m{usuario[1]}''')
            print(f'''\033[1;32mEmail: \033[0;0m{usuario[2]}''')
            print(f'''\033[1;32mSenha: \033[0;0m{usuario[3]}''')
            print(f'''\033[1;32mCelular: \033[0;0m{usuario[4]}''')
            print(f'''\033[1;32mEndereco: \033[0;0m{usuario[5]}''')
            print(f'''\033[1;32mTipoCliente: \033[0;0m{usuario[6]}''')
        criaBarra()
        valida = True
    else:
        valida = False

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha invalidos''\033[0;0m')
        criaBarra()
        subMenuClientes()


def usuariosCadastrados():
    limpaTerminal()
    print('''\033[1;32m=== Clientes Cadastrados ===\033[0;0m''')
    # Usuarios
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
    dados = """SELECT nome FROM cliente"""
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


def removerUsuario():
    try:
        limpaTerminal()
        print('=== << Remover Usuário >> ===')
        criaBarra()

        # Prompt for entering the client ID
        clienteID = input("\033[1;32mDigite o Cliente ID:\033[0;0m ")

        # Deletando todos os registros relacionados a tabela clienteID

        delete_movimentacao_query = f"""DELETE FROM movimentacao WHERE clienteIdUsuario = '{clienteID}' OR clienteIdInstituicao = '{clienteID}'"""
        delete_instituicao_query = f"DELETE FROM instituicao WHERE clienteId = '{clienteID}'"
        delete_alimentos_query = f"DELETE FROM alimento WHERE clienteId = '{clienteID}'"
        delete_usuario_query = f"DELETE FROM usuario WHERE clienteId = '{clienteID}'"
        delete_cliente_query = f"DELETE FROM cliente WHERE clienteId = '{clienteID}'"

        inst_SQL.execute(delete_movimentacao_query)
        inst_SQL.execute(delete_instituicao_query)
        inst_SQL.execute(delete_alimentos_query)
        inst_SQL.execute(delete_usuario_query)
        inst_SQL.execute(delete_cliente_query)

        conn.commit()
        print('\033[1;32mUsuário Excluído!\033[0;0m')
        criaBarra()
    except Exception as e:
        print(f"\033[1;31mErro ao remover usuário: {str(e)}\033[0;0m")
        criaBarra()

def userAdminValidate():
    limpaTerminal()
    criaBarra()
    print('\033[1;92m''Logue com o user e senha do administrador para administrar a plataforma''\033[0;0m')
    criaBarra()
    userLogin = input('Login: ')
    userSenha = input('Senha: ')

    # Variavel de validação do login
    valida = False

    logins = open('adminUser.txt', 'r')
    for linha in logins.readlines():
        valores = linha.split('-')
        print(valores)
        if userLogin == valores[0].split(':')[1].strip() and userSenha in valores[1].split(':')[1].strip():
            limpaTerminal()
            criaBarra()
            print(
                '\033[1;32m''Administrador Logado! Carregando dados...''\033[0;0m')
            criaBarra()
            sleep(3)
            valida = True
            break

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha invalidos''\033[0;0m')
        criaBarra()

    return valida


def cadastroInstituicao():
    try:
        limpaTerminal()
        print('====== < Cadastrar Instituicao > ======')
        clienteId = service.clienteID()
        nome = service.Nome()
        email = service.Email()
        senha = service.Senha()
        celular = service.Celular()
        endereco = service.endereco()
        tipoCliente = service.tipo_cliente()
        website = service.website()
        tipo = service.tipo()
        cnpj = service.cnpj()

        # Verificar se o clienteId existe na tabela cliente
        if clienteId is None:
            print('ClienteID não encontrado!')
            criaBarra()
            return

        # Verificar se a instituição já existe
        if service.confereInstituicaoExistente(clienteId):
            print('Instituicao já existente!')
            criaBarra()
            return

        # Executar o INSERT na tabela do SQL
        cadastroCliente = f"INSERT INTO cliente (clienteId, nome, email, senha, celular, endereco, tipoCliente) VALUES ('{clienteId}', '{nome}', '{email}', '{senha}', '{celular}', '{endereco}', '{tipoCliente}')"
        sqlInstituicao = f"INSERT INTO instituicao (clienteId, website, tipo, cnpj) VALUES ('{clienteId}', '{website}', '{tipo}', '{cnpj}')"

        try:
            inst_SQL.execute(cadastroCliente)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Erro ao cadastrar cliente: {e}")

        try:
            inst_SQL.execute(sqlInstituicao)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Erro ao cadastrar Instituicao: {e}")

        limpaTerminal()
        criaBarra()
        print('\033[1;32mCliente e Instituição cadastrados com sucesso!\033[0;0m')
        criaBarra()
    except ValueError:
        print("Digite valores numéricos")
    except Exception as e:
        print(f"Erro de transação com o BD: {e}")

def dadosInstituicao():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Instituicao''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Digite o código do Instituicao para ver dados!''\033[0;0m')
    criaBarra()
    id = input('id: ')

    # Variavel de validação do login
    valida = False

    dados = f"""SELECT * FROM Instituicao WHERE clienteid = '{id}'"""
    inst_SQL.execute(dados)
    listaInstituicao = inst_SQL.fetchall()
    if (len(listaInstituicao) != 0):
        limpaTerminal()
        criaBarra()
        print(
            '\033[1;32m''Instituicao encontrado! Dados do Instituicao: ''\033[0;0m')
        criaBarra()
        for Instituicao in listaInstituicao:
            print(f'''\033[1;32mClienteID: \033[0;0m{Instituicao[0]}''')

            print(f'''\033[1;32mWebsite: \033[0;0m{Instituicao[1]}''')

            print(f'''\033[1;32mTipo: \033[0;0m{Instituicao[2]}''')

            print(f'''\033[1;32mCnpj: \033[0;0m{Instituicao[3]}''')

        criaBarra()
        valida = True
        subMenuInstituicoes()

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! ID não encontrado ou inexistente.''\033[0;0m')
        criaBarra()
        subMenuInstituicoes()


def mostrarInstituicao():
    limpaTerminal()
    print('=== Instituicoes Cadastrados ===')
    dados = f"""SELECT * FROM Instituicao"""
    inst_SQL.execute(dados)
    listaInstituicoes = inst_SQL.fetchall()
    for Instituicao in listaInstituicoes:
        clienteid = Instituicao[0]
        website = Instituicao[1]
        tipo = Instituicao[2]
        cnpj = Instituicao[3]

        print(
            f'''\033[1;32mClienteID: \033[0;0m{clienteid} | \033[1;32mwebsite: \033[0;0m{website} 
            | \033[1;32mtipo: \033[0;0m{tipo} | \033[1;32mcnpj: \033[0;0m{cnpj}''')
    criaBarra()
    return
def relatorioInstituicao():
    limpaTerminal()
    arquivo = open('relatorioInstituicoes.txt', 'w+', encoding='utf-8')
    arquivo.write('Relatorio de Instituicoes \n')
    arquivo.write('\n')

    # Consulta SQL para obter os nomes dos usuários
    dados = """SELECT clienteid FROM Instituicao"""
    inst_SQL.execute(dados)
    listaNomes = inst_SQL.fetchall()

    countUsers = len(listaNomes)
    arquivo.write(f'A Alimenta-AI possui {countUsers} Instituicoes \n')
    for i, nome in enumerate(listaNomes, start=1):
        arquivo.write(f'{i}.{nome[0]} \n')
    criaBarra()
    print('\033[1;32m'"Relatorio gerado em 'relatorioInstituicoes.txt'"'\033[0;0m')
    criaBarra()
    arquivo.close()
    return


def gerenciarInstituicao():
    limpaTerminal()
    lista_dados = []
    id = input(
        f'''\033[1;32mDigite o código do Instituicao que deseja gerenciar: \033[0;0m''')
    consulta = f"""SELECT * FROM Instituicao WHERE clienteID = '{id}'"""
    inst_SQL.execute(consulta)
    dados = inst_SQL.fetchall()

    for dado in dados:
        lista_dados.append(dado)

        if (len(lista_dados) == 0):
            print(
                '\033[1;31m''Erro! Código não encontrado ou inexistente.''\033[0;0m')
        else:
            try:
                clienteID = input(f'''\033[1;32mDigite o novo Cliente ID: \033[0;0m''')
                website = input(f'''\033[1;32mDigite o novo website: \033[0;0m''')
                tipo = input(f'''\033[1;32mDigite o novo tipo: \033[0;0m''')
                cnpj = input(f'''\033[1;32mDigite o novo CNPJ: \033[0;0m''')
            except ValueError:
                print('\033[1;31m''Digite valores numericos''\033[0;0m')
            else:
                try:
                    str_update = f"""UPDATE Instituicao SET clienteID='{clienteID}', website='{website}' ,  tipo='{tipo}', 
                    CNPJ='{cnpj}' WHERE clienteid='{id}'"""
                    inst_SQL.execute(str_update)
                    conn.commit()
                except Exception as errobd:
                    print('\033[1;31m''Erro de transacao com o BD''\033[0;0m', errobd)
                else:
                    print(
                        f'''\033[1;32mDados alterados com sucesso\033[0;0m''')
    subMenuInstituicoes()


def removeInstituicao():
    limpaTerminal()
    print('=== << ''\033[1;33m''Dados do Instituicao''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Digite o código do Instituicao para excluir''\033[0;0m')
    criaBarra()
    id = input('id: ')

    valida = False

    dados = f"""SELECT * FROM Instituicao WHERE clienteID = '{id}'"""
    inst_SQL.execute(dados)
    listaInstituicao = inst_SQL.fetchall()
    if (len(listaInstituicao) != 0):
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Instituicao encontrado! Excluindo... ''\033[0;0m')
        criaBarra()
        sleep(5)
        # Excluir Instituicao
        delete_query = f"""DELETE FROM Instituicao WHERE clienteID = '{id}'"""
        inst_SQL.execute(delete_query)
        conn.commit()
        print('\033[1;32m''Instituicao Excluido! ''\033[0;0m')
        criaBarra()
        valida = True
    else:
        valida = False

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Código inválido ou inexistente''\033[0;0m')
        criaBarra()
        subMenuInstituicoes()
