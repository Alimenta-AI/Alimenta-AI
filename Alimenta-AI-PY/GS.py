from collections import OrderedDict
import random

class Totem:
    def __init__(self):
        self.menu = OrderedDict([
            (1, "Ver empresas cadastradas"),
            (2, "Informações sobre programas de assistência"),
            (3, "Solicitar doação"),
            (4, "Sair")
        ])

    def exibir_menu(self):
        print("=== Totem AlimentaAI ===")
        for opcao, descricao in self.menu.items():
            print(f"{opcao}. {descricao}")

    def selecionar_opcao(self):
        while True:
            opcao = int(input("Selecione uma opção: "))
            if opcao in self.menu:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")

    def ver_empresas_cadastradas(self):
        print("Empresas Cadastradas")
        print("1. ONG DA PAIXÃO")
        print("2. FOME ZERO")

    def ver_refeicoes_disponiveis(self):
        print("Refeições disponíveis:")
        print("1. Arroz")
        print("2. Feijão")
        print("3. Macarrão")
        print("4. Carne")

    def informacoes_programas_assistencia(self):
        print("Informações sobre programas de assistência:")
        print("1. Programa A")
        print("2. Programa B")
        print("3. Programa C")
        programa = int(input("Selecione um programa: "))

        if programa == 1:
            print("Programa A")
            print("- Observação: Este programa oferece assistência alimentar para crianças em idade escolar.")
        elif programa == 2:
            print("Programa B")
            print("- Observação: Este programa oferece assistência alimentar para famílias de baixa renda.")
        elif programa == 3:
            print("Programa C")
            print("- Observação: Este programa oferece assistência alimentar para idosos e pessoas com deficiência.")
        else:
            print("Opção inválida. Tente novamente.")

    def selecionar_empresa(self):
        while True:
            opcao = int(input("Selecione uma empresa: "))
            if opcao == 1:
                return "ONG DA PAIXÃO"
            elif opcao == 2:
                return "FOME ZERO"
            else:
                print("Opção inválida. Tente novamente.")

    def solicitar_doacao(self):
        resposta = input("Deseja fazer uma doação? (sim/não): ")
        if resposta.lower() == "sim":
            self.ver_empresas_cadastradas()
            empresa = self.selecionar_empresa()
            self.ver_refeicoes_disponiveis()
            refeicoes = self.selecionar_refeicoes()
            nomes = ["João", "Maria", "Pedro", "Ana", "Carlos"]
            nome_aleatorio = random.choice(nomes)
            print(f"Obrigado, {nome_aleatorio}, pela sua doação de {refeicoes} para {empresa}!")
        else:
            print("Agradecemos sua consideração!")

    def selecionar_refeicoes(self):
        refeicoes = []
        while True:
            opcao = int(input("Selecione uma refeição (0 para finalizar): "))
            if opcao == 0:
                break
            elif opcao == 1:
                refeicoes.append("Arroz")
            elif opcao == 2:
                refeicoes.append("Feijão")
            elif opcao == 3:
                refeicoes.append("Macarrão")
            elif opcao == 4:
                refeicoes.append("Carne")
            else:
                print("Opção inválida. Tente novamente.")
        return refeicoes

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = self.selecionar_opcao()

            if opcao == 1:
                self.ver_empresas_cadastradas()
            elif opcao == 2:
                self.informacoes_programas_assistencia()
            elif opcao == 3:
                self.solicitar_doacao()
            elif opcao == 4:
                print("Saindo do totem...")
                break
            else:
                print("Opção inválida. Tente novamente.")

totem = Totem()
totem.executar()
