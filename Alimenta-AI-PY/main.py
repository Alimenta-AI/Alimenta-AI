import random


def roleta_russa(participantes):
    indice_aleatorio = random.randint(0, len(participantes) - 1)
    print("Rodando a roleta russa...")
    print("Aperte Enter para continuar.")
    input()
    print("BANG!")
    print("O participante eliminado é:", participantes[indice_aleatorio])
    print("Restaram", len(participantes) - 1, "participantes.")


participantes = ["Matheus", "Thigas", "Shima", "Gab", "Felipe"]

roleta_russa(participantes)
