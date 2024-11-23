import random

class RamasseTout:
    CARTE = list(range(1, 105))  # Cartes numérotées de 1 à 104
    
    def __init__(self, joueurs):
        """Initialise le jeu avec les joueurs."""
        self.joueurs = {joueur: {'pioche': [], 'points': 0} for joueur in joueurs}
        self.rangées = []
        self.partie_terminée = False

    def calculer_penalite(self, carte):
        """Calcule la pénalité associée à une carte."""
        if carte == 55:
            return -7
        if carte % 11 == 0:
            return -5
        if carte % 10 == 0:
            return -3
        if carte % 5 == 0:
            return -2
        return -1

    def distribution(self):
        """Distribue 10 cartes à chaque joueur et initialise les rangées."""
        cartes_disponibles = self.CARTE[:]
        for joueur in self.joueurs:
            self.joueurs[joueur]['pioche'] = sorted(random.sample(cartes_disponibles, 10))
            for carte in self.joueurs[joueur]['pioche']:
                cartes_disponibles.remove(carte)
        
        # Initialiser 4 rangées avec des cartes aléatoires
        self.rangées = [[cartes_disponibles.pop(random.randint(0, len(cartes_disponibles) - 1))] for _ in range(4)]

        print("\nCartes initiales des joueurs :")
        for joueur, data in self.joueurs.items():
            print(f"{joueur} : {data['pioche']}")
        print(f"\nRangées initiales : {[rangée[0] for rangée in self.rangées]}")

    def trouver_rangée(self, carte):
        """Trouve la rangée la plus proche pour insérer une carte."""
        differences = [(r, carte - r[-1]) for r in self.rangées if carte > r[-1]]
        if not differences:
            return None  # Aucune rangée disponible
        rangée, _ = min(differences, key=lambda x: x[1])
        return rangée

    def jouer_carte(self, joueur, carte):
        """Joue une carte pour un joueur et gère les pénalités et les rangées."""
        rangée = self.trouver_rangée(carte)
        if rangée is None:  # Le joueur doit prendre une rangée
            print(f"{joueur} doit prendre une rangée.")
            for i, r in enumerate(self.rangées, 1):
                print(f"Rangée {i} : {r}")
            choix = int(input(f"{joueur}, choisissez une rangée (1-{len(self.rangées)}) : ")) - 1
            rangée_prise = self.rangées.pop(choix)
            self.joueurs[joueur]['points'] += sum(self.calculer_penalite(c) for c in rangée_prise)
            self.rangées.append([carte])  # La carte devient une nouvelle rangée
        else:  # Ajouter à la rangée
            rangée.append(carte)
            if len(rangée) > 5:  # La rangée est pleine
                print(f"La rangée est pleine, {joueur} doit la prendre.")
                self.joueurs[joueur]['points'] += sum(self.calculer_penalite(c) for c in rangée[:-1])
                carte_initiale = rangée[-1]
                self.rangées.remove(rangée)
                self.rangées.append([carte_initiale])

    def jouer_tour(self):
        """Un tour où chaque joueur joue une carte."""
        cartes_choisies = {}
        for joueur, data in self.joueurs.items():
            print(f"\n{joueur}, vos cartes : {data['pioche']}")
            carte = int(input(f"{joueur}, choisissez une carte à jouer : "))
            while carte not in data['pioche']:
                print("Carte invalide. Essayez encore.")
                carte = int(input(f"{joueur}, choisissez une carte à jouer : "))
            data['pioche'].remove(carte)
            cartes_choisies[joueur] = carte

        # Trier les joueurs par ordre de leurs cartes choisies
        for joueur, carte in sorted(cartes_choisies.items(), key=lambda x: x[1]):
            print(f"{joueur} joue la carte {carte}.")
            self.jouer_carte(joueur, carte)

        print("\nÉtat des rangées après ce tour :")
        for i, rangée in enumerate(self.rangées, 1):
            print(f"Rangée {i} : {rangée}")

    def manche_terminee(self):
        """Vérifie si une manche est terminée."""
        return all(len(data['pioche']) == 0 for data in self.joueurs.values())

    def fin_de_partie(self):
        """Vérifie si la partie est terminée (un joueur atteint -66 points)."""
        for joueur, data in self.joueurs.items():
            if data['points'] <= -66:
                self.partie_terminée = True
                print(f"\n{joueur} a atteint -66 points. La partie est terminée.")
                return True
        return False

    def jouer(self):
        """Boucle principale du jeu."""
        self.distribution()
        while not self.partie_terminée:
            while not self.manche_terminee():
                self.jouer_tour()
            print("\nFin de manche. Points actuels :")
            for joueur, data in self.joueurs.items():
                print(f"{joueur} : {data['points']} points")
            if self.fin_de_partie():
                break
            print("\n--- Nouvelle manche ---")
            self.distribution()


# Exemple d'utilisation
joueurs = ["Joueur1", "Joueur2", "Joueur3", "Joueur4"]
jeu = RamasseTout(joueurs)
jeu.jouer()


exect(

"""

"""    

)