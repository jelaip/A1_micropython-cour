
# declarer une variable 
a = 3

# declarer une fonction
def b(c):
    print(c+3)

# utiliser une fonction
b(a)

# boucle for
for x in range(a):
    print(x)

# boucle while
while a < 6:
    a+=1
    print(a)

#condition si 
if a == 6:
    print("a = 6")
# sinon 
else: 
    print("IIM")

# class bouteille
#1
class Bouteille:
    #2
    def __init__(self, taille,couleur):
        self.taille = taille
        self.couleur = couleur
        self.plein = True
    #3
    def vider(self):
        self.plein = False
    def remplir(self):
        self.plein = True

# creer une instance de la class bouteille
#4
bouteille = Bouteille(10,"rouge")

# utiliser une fonction de la class bouteille
#5
bouteille.vider()
print(bouteille.plein)
