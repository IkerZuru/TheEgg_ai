def tierra(tiempo):
    altura = 1/2 * 9.8 * (tiempo ** 2)
    print(f"Tierra : Si tarda {tiempo} segundos en caerse está a una altura de {altura} metros")

def marte(tiempo):
    altura = 1/2 * 3.7 * (tiempo ** 2)
    print(f"Marte : Si tarda {tiempo} segundos en caerse está a una altura de {altura} metros")

def jupiter(tiempo):
    altura = 1/2 * 24.8 * (tiempo ** 2)
    print(f"Jupiter :Si tarda {tiempo} segundos en caerse está a una altura de {altura} metros")

tierra(25)
marte(25)
jupiter(25)