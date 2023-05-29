import oracledb
import sys
import service
import datetime
import os
from time import sleep

try:
    dnStr = oracledb.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = oracledb.connect(user='rm97097', password='220104', dsn=dnStr)
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
    print(
        '=============== <<< ''\033[1;96m''Aliementa-AI''\033[0;0m'' >>> ===============')
    print(
        '|  [''\033[1;36m''1''\033[0;0m''] Clientes                                 |')
    print(
        '|  [''\033[1;36m''2''\033[0;0m''] Instituições                             |')
    print(
        '|  [''\033[1;36m''3''\033[0;0m''] Doação                                   |')
    print(
        '|  [''\033[1;36m''0''\033[0;0m''] Sair                                     |')
    print('------------------------------------------------')
    try:
        escolha = int(input('\033[1;36m''Insira a opção: ''\033[0;0m'))
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
        print('\033[1;36m''Fechando administração...''\033[0;0m')
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
    print('========== <<< ''\033[1;96m''Alimenta-AI''\033[0;0m'' >>> ==========')
    print(
        '|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Usuário              |')
    print(
        '|  [''\033[1;36m''2''\033[0;0m''] Dados do Usuário               |')
    print(
        '|  [''\033[1;36m''3''\033[0;0m''] Mostrar Usuários               |')

    print('|  [''\033[1;36m''4''\033[0;0m''] Gerar Relatório de Usuarios  |')

    print(
        '|  [''\033[1;36m''5''\033[0;0m''] Remover Usuário               |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Voltar                        |')
    print('--------------------------------------')
    try:
        escolha = int(input('\033[1;36m''Insira a opção: ''\033[0;0m'))
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
    print('========== <<< ''\033[1;96m''Alimenta-AI''\033[0;0m'' >>> ==========')
    print('|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Instituicao               |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Dados do Instituicao                |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Mostrar Instituicoes                |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Gerar Relatorio de Instituicoes     |')
    print('|  [''\033[1;36m''5''\033[0;0m''] Gerenciar Instituicao               |')
    print('|  [''\033[1;36m''6''\033[0;0m''] Remover Instituicao                 |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Voltar                        |')
    print('--------------------------------------')
    try:
        escolha = int(input('\033[1;36m''Insira a opção: ''\033[0;0m'))
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
        '============== <<< ''\033[1;96m''Alimenta-AI''\033[0;0m'' >>> ==============')
    print('|  [''\033[1;36m''1''\033[0;0m''] Tipos de Doacao                       |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Empresas                              |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Voltar                                |')
    print('----------------------------------------------')
    x = input('\033[1;36m''Insira a opção: ''\033[0;0m')
    print('----------------------------------------------')
    return x


''' Função de Cadastrar / Checar login existente / Adicionar dados no arquivo txt de logins '''


def confereLoginExistente(nome, login):
    dados = f"""SELECT * FROM usuario WHERE nome = '{nome}' OR nickname = '{login}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    if len(listaUsuario) != 0:
        return True
    else:
        return False


def cadastro():
    try:
        limpaTerminal()
        print('====== < ''\033[1;92m''Cadastrar Usuário''\033[0;0m'' > ======')

        nome = service.Nome()  # Retorna o nome validado
        login = service.User()  # Retorna o login validado

        if confereLoginExistente(nome, login):
            print('\033[1;31m''Login ja existente!''\033[0;0m')
            criaBarra()
            return

        # Retornando valores validados
        senha = service.Senha()
        email = service.Email()
        cpf = service.Cpf()
        endereco = service.endereco()
        clienteId = service.clienteID()
        tipoCliente = service.tipo_cliente()
        nascimento = ''.join(service.Data().split('/'))

        celular = service.Celular()

        # Executa o insert na tabela do sql

        cadastro1 = f"""INSERT INTO cliente (nome, email, senha, celular, endereco, clienteId, tipoCliente) VALUES ({nome}, {email}, {senha}, {celular}, {endereco}, {clienteId}, {tipoCliente} )"""
        cadastro2 = f"""INSERT INTO usuario (clienteId, cpf, nascimento) VALUES ({clienteId}, {cpf} , {nascimento})"""

        inst_SQL.execute(cadastro1)
        inst_SQL.execute(cadastro2)

        conn.commit()
        conn.close()
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Usuario Cadastrado com sucesso!''\033[0;0m')
        criaBarra()
        return
    except ValueError:
        print("Digite valores numéricos")
    except:
        print('\033[1;31m''Erro de transação com o BD''\033[0;0m')


''' Logar um usuário e printar seus dados cadastrados '''


def mostraDados():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Usuario''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Logue para acessar seus dados!''\033[0; 0m')
    criaBarra()
    userLogin = input('Login: ')
    userSenha = input('Senha: ')

    # Variavel de validação do login
    valida = False

    dados = f"""SELECT * FROM cliente WHERE nome = '{userLogin}' AND senha = '{userSenha}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    if (len(listaUsuario) != 0):
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Usuario Logado! Dados do usuário: ''\033[0; 0m')
        criaBarra()
        # Dados do usuario
        for usuario in listaUsuario:
            print(f'''\033[1;36mNome: \033[0;0m{usuario[1]}''')
            print(f'''\033[1;36mEmail: \033[0;0m{usuario[2]}''')
            print(f'''\033[1;36mSenha: \033[0;0m{usuario[3]}''')
            print(f'''\033[1;36mCelular: \033[0;0m{usuario[4]}''')
            print(f'''\033[1;36mEndereco: \033[0;0m{usuario[5]}''')
            print(f'''\033[1;36mClienteID: \033[0;0m{usuario[6]}''')
            print(f'''\033[1;36mTipoCliente: \033[0;0m{usuario[7]}''')
        criaBarra()
        valida = True
    else:
        valida = False

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha invalidos''\033[0; 0m')
        criaBarra()
        subMenuClientes()


def usuariosCadastrados():
    limpaTerminal()
    print('''\033[1;36m=== Clientes Cadastrados ===\033[0;0m''')
    # Usuarios
    dados = f"""SELECT * FROM usuario"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    for usuario in listaUsuario:
        nome = usuario[0]
        cpf = usuario[1]
        nascimento = usuario[2]
        print(
            f'''\033[1;36mNome: \033[0;0m{nome} | \033[1;36mcpf: \033[0;0m{cpf} | \033[1;36mNascimento: \033[0;0m{nascimento} ''')
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
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do cliente''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Logue para excluir seu cliente!''\033[0; 0m')
    criaBarra()
    userLogin = input('Login: ')
    userSenha = input('Senha: ')

    # Variavel de validação do login
    valida = False

    dados = f"""SELECT * FROM cliente WHERE nome = '{userLogin}' AND senha = '{userSenha}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    if (len(listaUsuario) != 0):
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Cliente Logado! Excluindo... ''\033[0; 0m')
        criaBarra()
        sleep(5)
        # Excluir usuario que logou
        delete_query = f"""DELETE FROM cliente WHERE nome = '{userLogin}'"""
        inst_SQL.execute(delete_query)
        conn.commit()
        print('\033[1;32m''Usuario Excluido! ''\033[0; 0m')
        criaBarra()
        valida = True
    else:
        valida = False

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha invalidos''\033[0; 0m')
        criaBarra()
        subMenuClientes()


def userAdminValidate():
    limpaTerminal()
    criaBarra()
    print('\033[1;96m''Logue com o user e senha do administrador para administrar a plataforma''\033[0;0m')
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
                '\033[1;32m''Administrador Logado! Carregando dados...''\033[0; 0m')
            criaBarra()
            sleep(3)
            valida = True
            break

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha invalidos''\033[0; 0m')
        criaBarra()

    return valida


def cadastroInstituicao():
    try:
        limpaTerminal()
        print('====== < ''\033[1;92m''Cadastrar Instituicao''\033[0;0m'' > ======')
        clienteId = service.clienteID()
        cnpj = service.cnpj()

        print(clienteId, cnpj)
        print(type(clienteId), type(cnpj))

        # Executa o insert na tabela do sql
        instituicaoCadastro = f"""INSERT INTO Instituicao (clienteId, cnpj) VALUES ({clienteId},{cnpj})"""
        inst_SQL.execute(instituicaoCadastro)
        conn.commit()
        conn.close()

        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Instituicao Cadastrado com sucesso!''\033[0;0m')
        criaBarra()
        subMenuInstituicoes()
    except ValueError:
        print("Digite valores numéricos")
    except:
        print('\033[1;31m''Erro de transação com o BD''\033[0;0m')


def dadosInstituicao():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Instituicao''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Digite o código do Instituicao para ver dados!''\033[0; 0m')
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
        print('\033[1;32m''Instituicao encontrado! Dados do Instituicao: ''\033[0; 0m')
        criaBarra()
        for Instituicao in listaInstituicao:
            print(f'''\033[1;36mClienteID: \033[0;0m{Instituicao[0]}''')
            print(f'''\033[1;36mCnpj: \033[0;0m{Instituicao[1]}''')


        criaBarra()
        valida = True
        subMenuInstituicoes()

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! ID não encontrado ou inexistente.''\033[0; 0m')
        criaBarra()
        subMenuInstituicoes()


def mostrarInstituicao():
    limpaTerminal()
    print('=== Instituicoes Cadastrados ===')
    dados = f"""SELECT * FROM Instituicao"""
    inst_SQL.execute(dados)
    listaInstituicoes = inst_SQL.fetchall()
    for Instituicao in listaInstituicoes:
        clienteid = Instituicao[1]
        cnpj = Instituicao[2]
        print(
            f'''\033[1;36mClienteID: \033[0;0m{clienteid} | \033[1;36mcnpj: \033[0;0m{cnpj} ''')
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
    id = input(f'''\033[1;36mDigite o código do Instituicao que deseja gerenciar: \033[0;0m''')
    consulta = f"""SELECT * FROM Instituicao WHERE clienteID = '{id}'"""
    inst_SQL.execute(consulta)
    dados = inst_SQL.fetchall()

    for dado in dados:
        lista_dados.append(dado)

        if (len(lista_dados) == 0):
            print('\033[1;31m''Erro! Código não encontrado ou inexistente.''\033[0; 0m')
        else:
            try:
                clienteID = input(f'''\033[1;36mDigite o novo Cliente ID: \033[0;0m''')
                cnpj = input(f'''\033[1;36mDigite o novo CNPJ: \033[0;0m''')
            except ValueError:
                print('\033[1;31m''Digite valores numericos''\033[0; 0m')
            else:
                try:
                    str_update = f"""UPDATE Instituicao SET clienteID='{clienteID}',CNPJ='{cnpj}' WHERE id_Instituicao='{id}'"""
                    inst_SQL.execute(str_update)
                    conn.commit()
                except:
                    print('\033[1;31m''Erro de transacao com o BD''\033[0; 0m')
                else:
                    print(f'''\033[1;32mDados alterados com sucesso\033[0;0m''')
    subMenuInstituicoes()


def removeInstituicao():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Instituicao''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Digite o código do Instituicao para excluir''\033[0; 0m')
    criaBarra()
    id = input('id: ')

    valida = False

    dados = f"""SELECT * FROM Instituicao WHERE clienteID = '{id}'"""
    inst_SQL.execute(dados)
    listaInstituicao = inst_SQL.fetchall()
    if (len(listaInstituicao) != 0):
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Instituicao encontrado! Excluindo... ''\033[0; 0m')
        criaBarra()
        sleep(5)
        # Excluir Instituicao
        delete_query = f"""DELETE FROM Instituicao WHERE clienteID = '{id}'"""
        inst_SQL.execute(delete_query)
        conn.commit()
        print('\033[1;32m''Instituicao Excluido! ''\033[0; 0m')
        criaBarra()
        valida = True
    else:
        valida = False

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Código inválido ou inexistente''\033[0; 0m')
        criaBarra()
        subMenuInstituicoes()
