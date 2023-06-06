import oracledb
import sys
import service
import datetime
import os
from time import sleep
import hashlib


try:
    dnStr = oracledb.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = oracledb.connect(user='rm96920', password='080903', dsn=dnStr)
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
    print(
        '------------------------------------------------------')
    print(
        '|  [''\033[1;32m''1''\033[0;0m''] Login                                         |')
    print(
        '|  [''\033[1;32m''2''\033[0;0m''] Cadastre-se                                   |')
    print(
        '------------------------------------------------------')

    try:
        escolha = int(input('\033[1;32m''Insira a opção: ''\033[0;0m'))
    except ValueError:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuAcesso()
        return
    print('------------------------------------------------')

    if escolha == 1:
        limpaTerminal()
        listaUsuario = login()
        if (len(listaUsuario) != 0):
            menuInicial(listaUsuario)
    elif escolha == 2:
        cadastro()
        menuAcesso()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuAcesso()

# Login


def login():
    limpaTerminal()
    criaBarra()
    print('\033[1;33m''Logue para acessar seus dados!''\033[0;0m')
    criaBarra()
    email = input('Seu melhor email: ')
    senha = hash_password(input('Senha: '))

    dados = f"""SELECT * FROM cliente WHERE email = '{email}' AND senha = '{senha}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    return listaUsuario


def check_password(password, hashed_password):
    hashed_input = hashlib.sha256(password.encode('utf-8')).hexdigest()[:20]
    return hashed_input == hashed_password

# Cadastro


def cadastro():
    try:
        limpaTerminal()
        print('====== < Cadastrar Usuário > ======')

        # Retornando valores validados
        clienteId = service.clienteID()
        clienteIdFixo = clienteId
        nome = service.Nome()
        email = service.Email()
        senha = hash_password(service.Senha())
        celular = service.Celular()
        endereco = service.endereco()
        cpf = service.Cpf()
        nascimento = ''.join(service.Data().split('/'))
        doador = "nao"
        tipoCliente = 0

        if confereLoginExistente(cpf):
            print('\033[1;31mLogin já existente!\033[0;0m')
            criaBarra()
            return

        # Executa o insert na tabela do SQL
        cadastroCliente = f"INSERT INTO cliente (clienteId, nome, email, senha, celular, endereco, tipoCliente) VALUES ('{clienteIdFixo}', '{nome}', '{email}', '{senha}', '{celular}', '{endereco}', {tipoCliente})"
        cadastroUsuario = f"INSERT INTO usuario (clienteId, cpf, nascimento, doador) VALUES ('{clienteIdFixo}', '{cpf}', '{nascimento}', '{doador}')"

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

        criaBarra()
        print('\033[1;32mUsuário cadastrado com sucesso!\033[0;0m')
        criaBarra()
    except ValueError:
        print("Digite valores numéricos")
    except Exception as e:
        print(f"Erro de transação com o BD: {e}")


def confereLoginExistente(cpf):
    dados = f"""SELECT * FROM usuario WHERE cpf = '{cpf}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    if len(listaUsuario) != 0:
        return True
    else:
        return False


def menuInicial(listaUsuario):
    limpaTerminal()
    print(
        '=============== <<< ''\033[1;92m''Bem vindo! Alimenta-AI''\033[0;0m'' >>> ===============')
    print(
        '|  [''\033[1;32m''1''\033[0;0m''] Meu Perfil                               |')
    print(
        '|  [''\033[1;32m''2''\033[0;0m''] Onde receber ajuda?                      |')
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
        subMenuClientes(listaUsuario)
    elif escolha == 2:
        print("dev")
    elif escolha == 0:
        print('\033[1;32m''Saindo...''\033[0;0m')
        sleep(3)
        menuAcesso()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuInicial()


def subMenuClientes(listaUsuario):
    print(
        '========== <<< ''\033[1;92m''Alimenta-AI''\033[0;0m'' >>> ==========')
    print(
        '|  [''\033[1;32m''1''\033[0;0m''] Dados do Usuário                 |')
    print(
        '|  [''\033[1;32m''2''\033[0;0m''] Atualizar meus dados             |')
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
        mostraDados(listaUsuario)
        subMenuClientes(listaUsuario)
    elif escolha == 2:
        gerenciarUsuario(listaUsuario)
        subMenuClientes(listaUsuario)
    elif escolha == 3:
        removerUsuario(listaUsuario)
        subMenuClientes(listaUsuario)
    elif escolha == 0:
        sleep(1)
        limpaTerminal()
        menuInicial(listaUsuario)
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        subMenuClientes(listaUsuario)


def mostraDados(listaUsuario):
    limpaTerminal()
    print('=== << ''\033[1;33m''Dados do Usuario''\033[0;0m'' >> ===')
    if (len(listaUsuario) != 0):
        # Dados do usuario
        for usuario in listaUsuario:
            print(f'''\033[1;32mNome: \033[0;0m{usuario[1]}''')
            print(f'''\033[1;32mEmail: \033[0;0m{usuario[2]}''')
            print(f'''\033[1;32mCelular: \033[0;0m{usuario[4]}''')
            print(f'''\033[1;32mEndereco: \033[0;0m{usuario[5]}''')
        criaBarra()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Ocorreu um erro.''\033[0;0m')
        criaBarra()
        subMenuClientes(listaUsuario)


def gerenciarUsuario(listaUsuario):
    limpaTerminal()
    clienteId = listaUsuario[0][0]

    if (len(listaUsuario) == 0):
        print(
            '\033[1;31m''Erro! Código não encontrado ou inexistente.''\033[0; 0m')
    else:
        try:
            nome = service.Nome()
            email = service.Email()
            senha = hash_password(service.Senha())
            celular = service.Celular()
            endereco = service.endereco()
            nascimento = ''.join(service.Data().split('/'))
        except ValueError:
            print('\033[1;31m''Digite valores válidos''\033[0; 0m')
        else:
            try:
                str_updateCliente = f"""UPDATE cliente SET nome='{nome}',email='{email}',senha='{senha}',celular='{celular}',endereco='{endereco}' WHERE clienteId='{clienteId}'"""
                str_updateUsuario = f"""UPDATE usuario SET nascimento='{nascimento}' WHERE clienteId='{clienteId}'"""
                inst_SQL.execute(str_updateCliente)
                inst_SQL.execute(str_updateUsuario)
                conn.commit()
            except:
                print('\033[1;31m''Erro de transacao com o BD''\033[0; 0m' + e)
            else:
                print(
                    f'''\033[1;32mDados alterados com sucesso\033[0;0m''')
    subMenuClientes(listaUsuario)


def hash_password(password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password[:20]


def removerUsuario(listaUsuario):
    try:
        limpaTerminal()
        print('=== << Remover Usuário >> ===')
        criaBarra()

        clienteId = listaUsuario[0][0]

        delete_movimentacao_query = f"""DELETE FROM movimentacao WHERE clienteIdUsuario = '{clienteId}'"""
        delete_usuario_query = f"DELETE FROM usuario WHERE clienteId = '{clienteId}'"
        delete_cliente_query = f"DELETE FROM cliente WHERE clienteId = '{clienteId}'"

        inst_SQL.execute(delete_movimentacao_query)
        inst_SQL.execute(delete_usuario_query)
        inst_SQL.execute(delete_cliente_query)

        conn.commit()
        print('\033[1;32mUsuário Excluído!\033[0;0m')
        criaBarra()
    except Exception as e:
        print(f"\033[1;31mErro ao remover usuário: {str(e)}\033[0;0m")
        criaBarra()

# Parei aqui 05/06/2023


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
