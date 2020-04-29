import random

class Baraja():
    palos = ('o','c','e','b')#atributo público
    cartas = ('A','2','3','4','5','6','7','S','C','R')

    def __init__(self):#método init
        self.__crea_baraja()

    def __crea_baraja(self):#método privado que nadie puede llamar fuera de la clase, ponemos 2 rayas delante del nombre
        self.naipes = [] #lista donde guardamos nuestra baraja
        self.mano = [] #lista para guardar nuestra mano
        for palo in self.palos:#bucle para ir agregando cartas a la baraja
            for carta in self.cartas:
                naipe = carta + palo
                self.naipes.append(naipe)#hasta aquí
    
    def mezclar(self):#método mezclar
        br = []

        while len(br) != len(self.naipes):    
            n = random.randint(0,len(self.naipes)-1)
            while self.naipes[n] in br:
                n = random.randint(0,len(self.naipes)-1)
            br.append(self.naipes[n])
        
        self.naipes[:] = br#recorre índice a índice y sustituye

    def repartir(self, players, cards):
        for p in range(players):
            self.mano.append([])

        for ic in range(cards):
            for ij in range(players):
                carta = self.naipes.pop(0)#extraemos carta de la baraja y asignamos a variable carta
                self.mano[ij].append(carta)#añadir carta a lista del jugador correspondiente
        
    
    def recoger(self):
        self.__crea_baraja()

if __name__ == "__main__":
    b = Baraja()
    b.mezclar()
    print("Naipes en clase",b.naipes)
