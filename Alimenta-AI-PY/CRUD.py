from time import sleep

import consult as consult
import oracledb as orcl
import pandas as pd

connection = False

try:
    # Abrindo conexão com o banco
    dsnStr = orcl.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = orcl.connect(user="RM97097", password="220104", dsn=dsnStr)

    inst_consult = conn.cursor()
    inst_register = conn.cursor()
    inst_update = conn.cursor()
    inst_delete = conn.cursor()

except Exception as e:
    # Se der erro retornará o motivo
    print("Erro: ", e)
    connection = False

else:
    connection = True

    # Usuário e senha para validação de usuário administrador
    user = input("DIGITE O USUÁRIO: ")
    password = input("DIGITE A SENHA: ")

while connection:
    # Se o usuário digitado for o de administrador...
    if user == "ADM" and password == "ADMIN123":
        try:
            opt = int(input("""\nMenu de administrador.
            1 - DADOS DOS USUÁRIOS.
            2 - DADOS DAS EMPRESAS.
            0 - SAIR
            DIGITE A OPÇÃO DESEJADA: """))

        except ValueError:
            print("Digite apenas o número da opção desejada.")
            sleep(2)

        else:
            # Usando a entidade de usuário
            if opt == 1:
                try:
                    opt = int(input("""\nQUAL AÇÃO DESEJA EXECUTAR NO USUÁRIO?
                1 - VISUALIZAR.
                2 - REGISTRAR.
                3 - ALTERAR.
                4 - EXCLUIR.
                QUAL OPÇÃO DESEJA SELECIONAR? """))

                except ValueError:
                    print("\nDigite apenas o número da opção desejada.")
                    sleep(2)

                # Visualizar os atributos dos usuários
                if opt == 1:
                    try:
                        dataList = []

                        inst_consult.execute('SELECT * FROM CLIENTE')

                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(oneData)

                        dataList = sorted(dataList)

                        dataDf = pd.DataFrame.from_records(dataList,
                                                           columns=['NOME', 'EMAIL', 'SENHA', 'CELULAR', 'ENDERECO',
                                                                    'CLIENTEID', 'TIPOCLIENTE']
                                                           )
                        if dataDf.empty:
                            print("Não há registros")
                            sleep(2)
                        else:
                            print(dataDf)
                            sleep(2)
                        print("\n")

                    except Exception as e:
                        print(e)
                        sleep(2)

                # Registrar um novo usuário
                elif opt == 2:
                    try:
                        nome = input("Digite o nome: ")
                        email = input("Digite o email: ")
                        senha = input("Digite a senha: ")
                        celular = input("digite o celular: ")
                        endereco = input("digite o endereco: ")
                        clienteId = input("digite o id: ")
                        tipoCliente = input("digite o tipo (PF ou PJ): ")

                        # Execute a instrução de registro no banco de dados

                        print("Usuário registrado com sucesso!")
                        sleep(2)

                    except Exception as e:
                        print(e)
                        sleep(2)

                # Alterar um usuário existente
                elif opt == 3:
                        dataList = []

                        cpf = input("Digite o CPF do usuário que você deseja alterar: ")

                        consult = f"""SELECT * FROM USUARIO WHERE CPF = '{cpf}'"""

                        inst_consult.execute(consult)
                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(oneData)

                        if len(dataList) == 0:
                            print("\nO CPF não existe.")
                            sleep(2)

                        else:
                            try:
                                opt = int(input("""
                1 - NOME
                2 - EMAIL
                3 - CEP
                4 - RUA
                5 - BAIRRO
                6 - UF
                7 - CPF
                8 - SENHA
                9 - DATA DE NASCIMENTO
                10 - CELULAR

                Qual dado você deseja alterar? """))

                            except ValueError:
                                print("\nDigite valores numéricos! ")
                                sleep(2)

                            # ALTERAR O NOME DO USUARIO
                            if opt == 1:
                                try:
                                    newName = input("\nNovo nome: ").upper()

                                    alter = f"""update USUARIO set NOME_USUARIO = '{newName}' where CPF = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            # ALTERAR O E-MAIL DO USUARIO
                            elif opt == 2:
                                try:
                                    newEmail = input("\nNovo E-MAIL: ").upper()

                                    alter = f"""update USUARIO set EMAIL = '{newEmail}' where CPF = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            # ALTERAR O CEP DO USUARIO
                            elif opt == 3:
                                try:
                                    newCep = int(input("\nNovo CEP: "))

                                    alter = f"""update USUARIO set CEP = {newCep} where CPF = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except ValueError:
                                    print("\nDigite um valor numérico.")
                                    sleep(2)

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            # ALTERAR A RUA DO USUARIO
                            elif opt == 4:
                                try:
                                    newRua = input("\nNova rua: ").upper()

                                    alter = f"""update USUARIO set RUA = '{newRua}' where CPF = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            # ALTERAR O BAIRRO DO USUARIO
                            elif opt == 5:
                                try:
                                    newBairro = input("\nNovo Bairro: ").upper()

                                    alter = f"""update USUARIO set BAIRRO = '{newBairro}' where CPF = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            # ALTERAR O UF DO USUARIO
                            elif opt == 6:
                                try:
                                    newUf = input("\nNova UF: ").upper()

                                    alter = f"""update USUARIO set UF = '{newUf}' where CPF = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            # ALTERAR O CPF DO USUARIO
                            elif opt == 7:
                                try:
                                    newCpf = int(input("\nNovo CPF: "))

                                    alter = f"""update USUARIO set CPF = '{newCpf}' where cpf = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            # ALTERAR A SENHA DO USUARIO
                            elif opt == 8:
                                try:
                                    newSenha = input("\nNova senha: ")

                                    alter = f"""update USUARIO set SENHA = '{newSenha}' where cpf = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            # ALTERAR A DATA DE NASCIMENTO DO USUARIO
                            elif opt == 9:
                                try:
                                    newDtNascimento = input("\nNova data de nascimento (DD/MM/AA): ")

                                    try:
                                        # Padronização de data para banco de dados
                                        listaData = newDtNascimento.split("/")

                                        listaMes = ["jan", "feb", "mar",
                                                    "apr", "may", "jun",
                                                    "jul", "aug", "sep",
                                                    "oct", "nov", "dec"]

                                        textoMes = listaMes[int(listaData[1]) - 1]
                                        newDtNascimento = f'{listaData[0]}-{textoMes}-{listaData[2]}'
                                    except:
                                        print("Insira uma data válida.")

                                    alter = f"""update USUARIO set DATA_NASC = '{newDtNascimento}' where cpf = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            # ALTERAR O CELULAR DO USUARIO
                            elif opt == 10:
                                try:
                                    newCel = int(input("\nNovo n° celular: "))

                                    alter = f"""update USUARIO set CEL = {newCel} where cpf = '{cpf}'"""

                                    inst_update.execute(alter)
                                    conn.commit()

                                except ValueError:
                                    print("\nDigite valores numéricos")
                                    sleep(2)

                                except:
                                    print("\nERRO banco de dados")
                                    sleep(2)

                                else:
                                    print("\nAtualização realizada!")
                                    sleep(2)

                            else:
                                print("\nDigite um  valor valido")
                                sleep(2)

                # Excluir um usuário existente
                elif opt == 4:
                    try:
                        cpf = input("Digite o CPF do usuário a ser excluído: ")

                        inst_consult.execute(consult)
                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(oneData)

                        if len(dataList) == 0:
                            print("\nO CPF não existe.")
                            sleep(2)


                        # Execute a instrução de exclusão no banco de dados

                        print("Usuário excluído com sucesso!")
                        sleep(2)


                    except Exception as e:
                        print(e)
                        sleep(2)

                else:
                    print("Opção inválida. Tente novamente.")
                    sleep(2)

            # Usando a entidade de empresas
            elif opt == 2:
                try:
                    opt = int(input("""\nQUAL AÇÃO DESEJA EXECUTAR NAS EMPRESAS?
                1 - VISUALIZAR.
                2 - REGISTRAR.
                3 - ALTERAR.
                4 - EXCLUIR.
                QUAL OPÇÃO DESEJA SELECIONAR? """))

                except ValueError:
                    print("\nDigite apenas o número da opção desejada.")
                    sleep(2)

                # Visualizar os atributos das empresas
                if opt == 1:
                    try:
                        dataList = []

                        inst_consult.execute('SELECT * FROM INSTUICAO')

                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(oneData)

                        dataList = sorted(dataList)

                        dataDf = pd.DataFrame.from_records(dataList,
                                                           columns=['CLIENTEID', 'CNPJ'],
                                                           index='CNPJ')
                        if dataDf.empty:
                            print("Não há registros")
                            sleep(2)
                        else:
                            print(dataDf)
                            sleep(2)
                        print("\n")


                    except Exception as e:
                        print(e)
                        sleep(2)

                # Registrar uma nova empresa
                elif opt == 2:
                    try:
                        nome = input("Digite o nome da empresa: ")
                        cnpj = input("Digite o CNPJ da empresa: ")
                        # Capture os demais atributos da empresa

                        # Execute a instrução de registro no banco de dados

                        print("Empresa registrada com sucesso!")
                        sleep(2)


                    except Exception as e:
                        print(e)
                        sleep(2)

                # Alterar uma empresa existente
                elif opt == 3:
                    try:
                        cnpj = input("Digite o CNPJ da empresa a ser alterada: ")
                        # Verifique se o CNPJ existe no banco de dados

                        # Capture os atributos a serem alterados

                        # Execute a instrução de atualização no banco de dados

                        print("Empresa alterada com sucesso!")
                        sleep(2)


                    except Exception as e:
                        print(e)
                        sleep(2)

                # Excluir uma empresa existente
                elif opt == 4:
                    try:
                        cnpj = input("Digite o CNPJ da empresa a ser excluída: ")
                        # Verifique se o CNPJ existe no banco de dados

                        # Execute a instrução de exclusão no banco de dados

                        print("Empresa excluída com sucesso!")
                        sleep(2)


                    except Exception as e:
                        print(e)
                        sleep(2)
                        # Execute a instrução de exclusão no banco de dados

                        print("Empresa excluída com sucesso!")
                        sleep(2)


                    except Exception as e:
                        print(e)
                        sleep(2)

                else:
                    print("Opção inválida. Tente novamente.")
                    sleep(2)

            # Sair do programa
            elif opt == 0:
                print("Saindo do programa...")
                break

            else:
                print("Opção inválida. Tente novamente.")
                sleep(2)

    else:
        print("Usuário ou senha inválidos. Tente novamente.")
        break
# Bloco finally para fechar a conexão

try:

    if connection:
        conn.close()


except Exception as e:

    print("Erro ao fechar a conexão: ", e)