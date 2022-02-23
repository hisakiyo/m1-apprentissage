import random

class Agent:
    def __init__(self, vlambda, ile):
        self.vlambda = vlambda
        self.q = []
        self.ile = ile
        self.init_matrix()
    
    def init_matrix(self):
        self.q = self.ile.calculer_matrice_etat_actions()
        # For into self.q and set all values to 0 
        for i in range(self.ile.taille):
            for j in range(self.ile.taille):
                for k in range(4):
                    if self.q[i][j][k] != -1:
                        self.q[i][j][k] = 0

    def update_q(self, etat, action, reward):
        self.q[etat[0]][etat[1]][action] += self.vlambda * (reward - self.q[etat[0]][etat[1]][action])
        print('ajouté :', self.vlambda * (reward - self.q[etat[0]][etat[1]][action]))
        return self.ile.etat_suivant(etat, action)

    # In Qtable, find the best action for the current state
    def choisir_action(self, etat):
        # Get possible actions
        action = self.q[etat[0]][etat[1]].index(max(self.q[etat[0]][etat[1]]))
        if self.q[etat[0]][etat[1]][action] == 0:
            action = random.randint(0, 3)
        print('State :', self.q[etat[0]][etat[1]])
        if action == 0:
            return 'N'
        elif action == 1:
            return 'S'
        elif action == 2:
            return 'E'
        elif action == 3:
            return 'O'



class Ile:
    def __init__(self, taille=10, nb_rhum=3, position_joueur=[0, 0]):
        self.matrice = []
        self.taille = taille
        self.nb_rhum = nb_rhum
        self.nb_tresor = 1
        self.position_joueur = position_joueur
        self.steps = 0
        self.max_steps = 20000
    
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

    def etat_suivant(self, etat, action):
        if action == 'N':
            return etat[0] - 1, etat[1]
        elif action == 'S':
            return etat[0] + 1, etat[1]
        elif action == 'E':
            return etat[0], etat[1] + 1
        elif action == 'O':
            return etat[0], etat[1] - 1
        else:
            return etat

    def mouvement_joueur(self, direction):
        # Get next coordinates with etat_suivant
        next_etat = self.etat_suivant(self.position_joueur, direction)
        # Check if next coordinates are in the map
        print('next_etat :', next_etat)
        print('matrice :', self.matrice)
        if self.matrice[next_etat[0]][next_etat[1]] == 10:
            print('Tresor trouvé !')
            exit()
        if self.steps < self.max_steps:
            if direction == 'N':
                if self.position_joueur[0] > 0:
                    self.matrice[self.position_joueur[0]][self.position_joueur[1]] = 0
                    self.position_joueur[0] -= 1
                    self.steps += 1
            elif direction == 'S':
                if self.position_joueur[0] < self.taille - 1:
                    self.matrice[self.position_joueur[0]][self.position_joueur[1]] = 0
                    self.position_joueur[0] += 1
                    self.steps += 1
            elif direction == 'E':
                if self.position_joueur[1] < self.taille - 1:
                    self.matrice[self.position_joueur[0]][self.position_joueur[1]] = 0
                    self.position_joueur[1] += 1
                    self.steps += 1
            elif direction == 'O':
                if self.position_joueur[1] > 0:
                    self.matrice[self.position_joueur[0]][self.position_joueur[1]] = 0
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
    agent = Agent(0.9, ile)
    choosen_path = []
    for step in range(ile.max_steps):
        print(ile)
        print("Actions possibles: ", ile.actions_possibles())
        action = agent.choisir_action(ile.position_joueur)
        print("Action choisie: ", action)
        choosen_path.append(action)
        ile.mouvement_joueur(action)
        print("Position du joueur: ", ile.position_joueur)
        print("Nombre de pas: ", ile.steps)
        reward = ile.matrice[ile.position_joueur[0]][ile.position_joueur[1]]
        etat = ile.position_joueur
        # determine action idx
        action_idx = 0
        if action == 'N':
            action_idx = 0
        elif action == 'S':
            action_idx = 1
        elif action == 'E':
            action_idx = 2
        elif action == 'O':
            action_idx = 3
        print("Reward: ", reward)
        print("Path: ", choosen_path)
        print(agent.q)
        agent.update_q(etat, action_idx, reward)
        print("\n")

    # Fill qtable

def main():
    ile = Ile(10)
    ile.generer_ile()
    qlearning(ile)
    

if __name__ == '__main__':
    main()