import random


# Classe Ile représentant une ile du jeu avec une matrice
class Ile:
    def __init__(self, taille=10, nb_rhum=1, position_joueur=[0, 0]):
        self.matrice = []
        self.taille = taille
        self.nb_rhum = nb_rhum
        self.nb_tresor = 1
        self.position_joueur = position_joueur
        self.steps = 0
        self.max_steps = 20
    
    def init_matrice(self):
        for i in range(self.taille):
            self.matrice.append([])
            for j in range(self.taille):
                self.matrice[i].append(0)
    
    def generer_tresor(self):
        for i in range(self.nb_tresor):
            x = random.randint(0, self.taille - 1)
            y = random.randint(0, self.taille - 1)
            while self.matrice[x][y] == 10:
                x = random.randint(0, self.taille - 1)
                y = random.randint(0, self.taille - 1)
            self.matrice[x][y] = 10

    def generer_rhum(self):
        for i in range(self.nb_rhum):
            x = random.randint(0, self.taille - 1)
            y = random.randint(0, self.taille - 1)
            while self.matrice[x][y] == 2:
                x = random.randint(0, self.taille - 1)
                y = random.randint(0, self.taille - 1)
            self.matrice[x][y] = 2
    
    def generer_ile(self):
        self.init_matrice()
        self.generer_tresor()
        self.generer_rhum()

    def changer_taille(self, taille):
        self.taille = taille
        self.generer_ile()
    
    def changer_nb_rhum(self, nb_rhum):
        self.nb_rhum = nb_rhum
        self.generer_ile()

    def actions_possibles(self):
        actions = []
        if self.position_joueur[0] > 0:
            actions.append('N')
        if self.position_joueur[0] < self.taille - 1:
            actions.append('S')
        if self.position_joueur[1] > 0:
            actions.append('O')
        if self.position_joueur[1] < self.taille - 1:
            actions.append('E')
        return actions

    def actions_possibles_coordonnees(self, x, y):
        actions = []
        if x > 0:
            actions.append('N')
        if x < self.taille - 1:
            actions.append('S')
        if y > 0:
            actions.append('O')
        if y < self.taille - 1:
            actions.append('E')
        return actions

    def action_aleatoire_possible(self):
        actions = self.actions_possibles()
        if len(actions) > 0:
            return random.choice(actions)
        else:
            return None

    # calcul de la matrice etat/action en listant les états possibles et en récupérant la valeur des actions avec actions_possibles_coordonnees
    def calculer_matrice_etat_actions(self):
        matrice_etat_actions = []
        for i in range(self.taille):
            matrice_etat_actions.append([])
            for j in range(self.taille):
                matrice_etat_actions[i].append([])
                actions_possibles = self.actions_possibles_coordonnees(i, j)
                for l in ['N', 'S', 'E', 'O']:
                    if l in actions_possibles:
                        if l == 'N':
                            matrice_etat_actions[i][j].append(self.matrice[i - 1][j])
                        elif l == 'S':
                            matrice_etat_actions[i][j].append(self.matrice[i + 1][j])
                        elif l == 'E':
                            matrice_etat_actions[i][j].append(self.matrice[i][j + 1])
                        elif l == 'O':
                            matrice_etat_actions[i][j].append(self.matrice[i][j - 1])
                    else:
                        matrice_etat_actions[i][j].append(-1)


        return matrice_etat_actions

    # Fonction qui retourne un nouvel état en fonction d'un état et d'une action
    

    def mouvement_joueur(self, direction):
        if self.steps < self.max_steps:
            if direction == 'N':
                if self.position_joueur[0] > 0:
                    self.position_joueur[0] -= 1
                    self.steps += 1
            elif direction == 'S':
                if self.position_joueur[0] < self.taille - 1:
                    self.position_joueur[0] += 1
                    self.steps += 1
            elif direction == 'E':
                if self.position_joueur[1] < self.taille - 1:
                    self.position_joueur[1] += 1
                    self.steps += 1
            elif direction == 'O':
                if self.position_joueur[1] > 0:
                    self.position_joueur[1] -= 1
                    self.steps += 1
            else:
                print("Mouvement non valide")
        else:
            print("Vous avez atteint le nombre de pas maximum")

    def __str__(self):
        return str(self.matrice)

# Implémentation de l'algorithme egreedy
def egreedy(ile, epsilon):
    if random.random() < epsilon:
        return ile.action_aleatoire_possible()
    else:
        return ile.actions_possibles()[0]

def run_egreedy(ile):
    for step in range(ile.max_steps):
        print(ile)
        print("Actions possibles: ", ile.actions_possibles())
        action = egreedy(ile, 0.1)
        print("Action choisie: ", action)
        ile.mouvement_joueur(action)
        print("Position du joueur: ", ile.position_joueur)
        print("Nombre de pas: ", ile.steps)
        print("\n")

def qlearning(ile):
    qtable = []
    for i in range(ile.taille):
        qtable.append([])
        for j in range(ile.taille):
            qtable[i].append([])
            for k in range(4):
                qtable[i][j].append(0)

    # Fill qtable

def main():
    ile = Ile(5)
    ile.generer_ile()
    print(ile.matrice)
    print(ile.calculer_matrice_etat_actions())
    

if __name__ == '__main__':
    main()