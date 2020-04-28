"""pendiente convertir en clase: crea_baraja como init y como métodos la función mezclar y la función repartir"""

import random

palos = ('o','c','e','b')
cartas = ('A','2','3','4','5','6','7','S','C','R')


def crea_baraja():
    baraja = []

    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append(naipe)

    return baraja

def mezclar(b):#falta arreglo para que no duplique listas
    br = []
    i = 0
    while i < 40:
        n = random.randint(0,39)
        while b[n] in br:
            n = random.randint(0,39)
        br.append(b[n])
        i += 1
    b = br
    return b 
    

def repartir(b, players, cards):
    res = [] 
    for p in range(players):
        res.append([])
    for ic in range(cards):
        for ij in range(players):
            carta = b.pop(0)#extraemos carta de la baraja y asignamos a variable carta
            res[ij].append(carta)#añadir carta a lista del jugador correspondiente
    
    return res



"""falta subir proyecto en git"""