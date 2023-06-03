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


def menuAcesso():
    limpaTerminal()
    print(
        '|  [''\033[1;32m''1''\033[0;0m''] Login                                         |')
    print(
        '|  [''\033[1;32m''2''\033[0;0m''] Cadastre-se                                   |')

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
        if (len(login()) != 0):
            menuInicial()
    elif escolha == 2:
        limpaTerminal()
        cadastro()
        menuAcesso()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuInicial()


def menuInicial():
    limpaTerminal()
    print(
        '=============== <<< ''\033[1;92m''Bem vindo! Alimenta-AI''\033[0;0m'' >>> ===============')
    print(
        '|  [''\033[1;32m''1''\033[0;0m''] Clientes                                 |')
    print(
        '|  [''\033[1;32m''2''\033[0;0m''] Doação                                   |')
    print(
        '|  [''\033[1;32m''0''\033[0;0m''] Sair                                     |')
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
        subMenuDoacao()
    elif escolha == 0:
        print('\033[1;32m''Saindo...''\033[0;0m')
        conn.close()
        sleep(3)
        menuAcesso()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuInicial()

# MATHEUS PAROU O DEV AQUI!


def subMenuClientes():
    print(
        '========== <<< ''\033[1;92m''Alimenta-AI''\033[0;0m'' >>> ==========')
    print(
        '|  [''\033[1;32m''1''\033[0;0m''] Dados do Usuário                 |')
    print(
        '|  [''\033[1;32m''2''\033[0;0m''] Mostrar Instituições cadastradas |')
    print(
        '|  [''\033[1;32m''3''\033[0;0m''] Deletar minha conta              |')
    print(
        '|  [''\033[1;32m''0''\033[0;0m''] Voltar                           |')
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
        mostraDados()
        subMenuClientes()
    elif escolha == 2:

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
        f'''\033[1;32mDigite o clienteID que deseja gerenciar: \033[0;0m''')
    consultaInstituicao = f"""SELECT * FROM Instituicao WHERE clienteID = '{id}'"""
    inst_SQL.execute(consultaInstituicao)
    dados = inst_SQL.fetchall()

    for dado in dados:
        lista_dados.append(dado)

        if (len(lista_dados) == 0):
            print(
                '\033[1;31m''Erro! Código não encontrado ou inexistente.''\033[0;0m')
        else:
            try:
                print(
                    '\n\033[1;31m''=== Alterando dados de Instituição ===''\033[0;0m')

                website = input(
                    f'''\033[1;32mDigite o novo website: \033[0;0m''')
                tipo = input(f'''\033[1;32mDigite o novo tipo: \033[0;0m''')
                cnpj = input(f'''\033[1;32mDigite o novo CNPJ: \033[0;0m''')

            except ValueError:
                print('\033[1;31m''Digite valores numericos''\033[0;0m')
            else:
                try:
                    updateInstituicao = f"""UPDATE Instituicao SET website='{website}' ,  tipo='{tipo}', 
                    CNPJ='{cnpj}' WHERE clienteid='{id}'"""
                    inst_SQL.execute(updateInstituicao)
                    conn.commit()
                except Exception as errobd:
                    print(
                        '\033[1;31m''Erro de transacao com o BD''\033[0;0m', errobd)
                else:
                    print(
                        f'''\033[1;32mInstituicao alterada com sucesso\033[0;0m''')
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


def login():
    limpaTerminal()
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
    return listaUsuario
