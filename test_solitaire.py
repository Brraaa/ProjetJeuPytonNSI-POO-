import pygame

# Initialisation de Pygame
pygame.init()

# Définition de la classe Boutique
class Boutique:
    def __init__(self, items):
        self.items = items

    def afficher(self):
        for i, objet in enumerate(self.items):
            y = 100 + i * 50
            pygame.draw.rect(fenetre, (0, 0, 255), (50, y, 200, 40))  # Boîte d'objet
            font = pygame.font.Font(None, 36)
            text = font.render(objet["name"] + f" - {objet['prix']} pièces d'or", True, (255, 255, 255))
            fenetre.blit(text, (60, y + 5))

    def acheter_objet(self, joueur, objet):
        if joueur.argent >= objet["prix"]:
            joueur.argent -= objet["prix"]
            joueur.inventaire.append(objet)
            print(f"Vous avez acheté {objet['name']}!")
            self.items.remove(objet)
        else:
            print("Vous n'avez pas assez d'argent pour acheter cet objet.")

    def vendre_objets(self, joueur, objets):
        for objet in objets:
            if objet in joueur.inventaire:
                joueur.inventaire.remove(objet)
                joueur.argent += objet["prix"]
                self.items.append(objet)
                print(f"Vous avez vendu {objet['name']} pour {objet['prix']} pièces d'or!")
            else:
                print("Vous ne possédez pas cet objet.")

# Définition de la classe Joueur
class Joueur:
    def __init__(self, argent):
        self.argent = argent
        self.inventaire = []
        self.niveau_experience = 1

    def gagner_experience(self, experience_gagnee):
        self.niveau_experience += experience_gagnee

# Initialisation de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Boutique RPG")

# Liste des objets en vente dans la boutique
boutique_items = [
    {"name": "Épée en fer", "description": "Une épée en fer de qualité supérieure.", "prix": 50, "dégâts": 10},
    {"name": "Armure en cuir", "description": "Une armure légère en cuir.", "prix": 30, "défense": 5}
]

# Création d'une instance de la boutique
boutique = Boutique(boutique_items)

# Création d'une instance du joueur
joueur = Joueur(100)  # Le joueur commence avec 100 pièces d'or

# Boucle de jeu
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche de la souris
                x, y = event.pos  # Coordonnées du clic de souris

                # Vérifier si le joueur a cliqué sur un objet dans la boutique
                for objet in boutique.items:
                    y_objet = 100 + boutique.items.index(objet) * 50
                    if 50 <= x <= 250 and y_objet <= y <= y_objet + 40:
                        boutique.acheter_objet(joueur, objet)

                # Vérifier si le joueur a cliqué sur un objet dans son inventaire
                for objet in joueur.inventaire:
                    y_objet = 100 + joueur.inventaire.index(objet) * 50
                    if 350 <= x <= 550 and y_objet <= y <= y_objet + 40:
                        boutique.vendre_objets(joueur, [objet])

    # Afficher le contenu de la boutique
    boutique.afficher()

    # Afficher l'inventaire du joueur
    for i, objet in enumerate(joueur.inventaire):
        y = 100 + i * 50
        pygame.draw.rect(fenetre, (0, 255, 0), (350, y, 200, 40))  # Boîte d'objet
        font = pygame.font.Font(None, 36)
        text = font.render(objet["name"], True, (255, 255, 255))
        fenetre.blit(text, (360, y + 5))

    # Afficher le niveau d'expérience du joueur
    font = pygame.font.Font(None, 36)
    text = font.render(f"Niveau d'expérience : {joueur.niveau_experience}", True, (255, 255, 255))
    fenetre.blit(text, (50, 50))

    pygame.display.update()
