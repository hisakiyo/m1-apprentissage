from os import write
import random

#Créer une structure Neurone, contenant 3 champs : le biais (réel), la sortie (entier) et le tableau de poids (réels).
class Neurone:
    def __init__(self, nb_poids):
        self.biais = 0
        self.sortie = 0
        self.poids = [0 for i in range(nb_poids)]
        self.pas = 0.01
    # Fonction d'initialisation des neurones
    def init_neurone(self):
        self.biais = 0.5
        self.sortie = 0
        for i in range(len(self.poids)):
            self.poids[i] = random.uniform(0, 1)
    # Fonction de calcul de la sortie d'un neurone
    def calcul_valeur_neurone(self, exemple):
        somme = 0
        for i in range(len(exemple)):
            somme += self.poids[i] * exemple[i]
        somme -= self.biais
        if somme > 0:
            self.sortie = 1
        else:
            self.sortie = -1
    


def generate_data(n):
    data = []
    for i in range(n):
        x1 = random.random()
        x2 = random.random()
        tag = 1 if x1 + x2 - 1 > 0 else -1
        data.append((x1, x2, tag))
    return data

# écrire les données dans un fichier sous la forme x1 x2 tag
def write_data(data, fileName):
    file = open(fileName, "w")
    for d in data:
        file.write(str(d[0]) + " " + str(d[1]) + " " + str(d[2]) + "\n")
    file.close()

write_data(generate_data(50), "data.txt")
# Test neurone
neurone = Neurone(2)
neurone.init_neurone()
print(neurone.biais)