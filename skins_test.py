import pygame
import sys
from player import Player

class Skin(Player):
    def __init__(self, image_path):
        self.player = Player((300,300),self.display_surface,self.create_jump_particles)


class Game:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()

        # Définir la taille de la fenêtre
        self.largeur, self.hauteur = 800, 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Choix du Skin")

        # Charger les skins
        self.skins = [Skin(f"graphics\character\idle/{i}.png") for i in range(1, 6)]
        self.skin_index = 1

        # Sélection par défaut
        self.skin_actuel = self.skins[self.skin_index]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Vérifier si le clic est sur le bouton de changement de skin
                    x, y = pygame.mouse.get_pos()
                    if 100 <= x <= 200 and 100 <= y <= 200:
                        # Changer le skin
                        self.skin_index = (self.skin_index + 1) % len(self.skins)
                        self.skin_actuel = self.skins[self.skin_index]

            # Effacer l'écran
            self.fenetre.fill((255, 255, 255))

            # Afficher le skin actuel
            self.fenetre.blit(self.skin_actuel.image, (300, 300))

            # Afficher le bouton de changement de skin
            pygame.draw.rect(self.fenetre, (0, 0, 255), (100, 100, 100, 100))

            # Mettre à jour l'affichage
            pygame.display.flip()

        # Quitter Pygame
        pygame.quit()
        sys.exit()

# Instancier et exécuter le jeu
jeu = Game()
jeu.run()