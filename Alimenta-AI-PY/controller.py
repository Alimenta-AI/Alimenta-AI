import oracledb
import sys
import service
import datetime
import os
from time import sleep
import hashlib


try:
    dnStr = oracledb.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = oracledb.connect(user='rm97121', password='290603', dsn=dnStr)
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
        else:
            print('\033[1;31m''Dados inválidos''\033[0;0m')
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
        '|  [''\033[1;32m''3''\033[0;0m''] Relatórios do projeto                    |')
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
        limpaTerminal()
        menuAjuda(listaUsuario)
    elif escolha == 3:
        limpaTerminal()
        relatorios(listaUsuario)
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
        menuAcesso()
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
                listaUsuario = [
                    (clienteId, nome, email, senha, celular, endereco, 0)]
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


def menuAjuda(listaUsuario):
    print(
        '========== <<< ''\033[1;92m''A Alimenta-AI pode te ajudar!''\033[0;0m'' >>> ==========')
    print(
        '|  [''\033[1;32m''1''\033[0;0m''] Instituições que estão em nossa plataforma         |')
    print(
        '|  [''\033[1;32m''2''\033[0;0m''] Apenas os endereços das instituições               |')
    print(
        '|  [''\033[1;32m''3''\033[0;0m''] Solicitar comida neste ponto de encontro           |')
    print(
        '|  [''\033[1;32m''0''\033[0;0m''] Voltar                                             |')
    print('-----------------------------------------------------------')
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
        mostrarInstituicoes()
        menuAjuda(listaUsuario)
    elif escolha == 2:
        mostrarNomeEnderecoInstituicoes()
        menuAjuda(listaUsuario)
    elif escolha == 3:
        print(f'''\033[1;32mSua solicitação de ajuda foi enviada e a instituição disponível irá ajuda-la! Aguarde para mais informações...''')
        sleep(3)
        menuAjuda(listaUsuario)
    elif escolha == 0:
        sleep(1)
        limpaTerminal()
        menuInicial(listaUsuario)
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuAjuda(listaUsuario)


def mostrarInstituicoes():
    limpaTerminal()
    print('\033[1;32m=== Instituições Cadastradas ===\033[0;0m')
    query = "SELECT * FROM cliente WHERE tipoCliente = 1"
    inst_SQL.execute(query)
    clientes = inst_SQL.fetchall()

    for cliente in clientes:
        clienteId = cliente[0]
        nome = cliente[1]
        email = cliente[2]
        senha = cliente[3]
        celular = cliente[4]
        endereco = cliente[5]

        print(f"\033[1;32mClienteID: {clienteId}\033[0;0m")
        print(f"\033[1;32mNome: {nome}\033[0;0m")
        print(f"\033[1;32mE-mail: {email}\033[0;0m")
        print(f"\033[1;32mSenha: {senha}\033[0;0m")
        print(f"\033[1;32mCelular: {celular}\033[0;0m")
        print(f"\033[1;32mEndereço: {endereco}\033[0;0m")

        print('\033[1;32m=== Dados da Instituição ===\033[0;0m')
        query = f"SELECT * FROM instituicao WHERE clienteId = '{clienteId}'"
        inst_SQL.execute(query)
        instituicoes = inst_SQL.fetchall()

        for instituicao in instituicoes:
            website = instituicao[0]
            tipo = instituicao[1]
            cnpj = instituicao[2]

            print(f"\033[1;32mWebsite: {website}\033[0;0m")
            print(f"\033[1;32mTipo: {tipo}\033[0;0m")
            print(f"\033[1;32mCNPJ: {cnpj}\033[0;0m")

        print("==============================")

    return


def mostrarNomeEnderecoInstituicoes():
    limpaTerminal()
    print('\033[1;32m=== Instituições Cadastradas ===\033[0;0m')
    query = "SELECT c.nome, c.endereco, i.cnpj FROM cliente c JOIN instituicao i ON c.clienteId = i.clienteId WHERE c.tipoCliente = 1"
    inst_SQL.execute(query)
    instituicoes = inst_SQL.fetchall()

    for instituicao in instituicoes:
        nome = instituicao[0]
        endereco = instituicao[1]
        cnpj = instituicao[2]

        print(f"\033[1;32mNome: {nome}\033[0;0m")
        print(f"\033[1;32mEndereço: {endereco}\033[0;0m")
        print(f"\033[1;32mCNPJ: {cnpj}\033[0;0m")
        criaBarra()

    return


def relatorios(listaUsuario):
    relatorio_cliente()
    relatorio_usuario()
    relatorio_instituicao()
    relatorio_estoque()
    relatorio_alimento()
    relatorio_movimentacao()
    relatorio_avaliacao()
    relatorio_comentario()
    relatorio_reserva_cliente()
    return


def executar_consulta(query):
    inst_SQL.execute(query)
    resultado = inst_SQL.fetchall()
    colunas = [desc[0] for desc in inst_SQL.description]
    print('\033[1m' + ' | '.join(colunas) + '\033[0m')
    for linha in resultado:
        # Converter os valores em strings
        valores_formatados = [str(valor) for valor in linha]
        # Imprimir os valores separados por |
        print(' | '.join(valores_formatados))

    return


# Consulta na tabela cliente


def relatorio_cliente():
    query = "SELECT * FROM cliente WHERE tipoCliente = 1"
    executar_consulta(query)

# Consulta na tabela usuario


def relatorio_usuario():
    query = "SELECT * FROM usuario WHERE doador = 'SIM'"
    executar_consulta(query)

# Consulta na tabela instituicao


def relatorio_instituicao():
    query = "SELECT * FROM instituicao WHERE tipo = 'ONG'"
    executar_consulta(query)

# Consulta na tabela estoque


def relatorio_estoque():
    query = "SELECT * FROM estoque WHERE tamanho > 100"
    executar_consulta(query)

# Consulta na tabela alimento


def relatorio_alimento():
    query = "SELECT * FROM alimento WHERE quantidade > 8"
    executar_consulta(query)

# Consulta na tabela movimentacao


def relatorio_movimentacao():
    query = "SELECT * FROM movimentacao WHERE categoria = 'Faz Doação'"
    executar_consulta(query)

# Consulta na tabela avaliacao


def relatorio_avaliacao():
    query = "SELECT * FROM avaliacao WHERE nota >= 4"
    executar_consulta(query)

# Consulta na tabela comentario


def relatorio_comentario():
    query = "SELECT * FROM comentario WHERE dataComentario = '20230508'"
    executar_consulta(query)

# Consulta na tabela reservaCliente


def relatorio_reserva_cliente():
    query = "SELECT * FROM reservaCliente WHERE clienteId = 'CLT001'"
    executar_consulta(query)
