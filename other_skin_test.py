import pygame
import sys
from tiles import Tile

class Skin:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)

class Game:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()

        # Définir la taille de la fenêtre
        self.largeur, self.hauteur = 800, 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Choix du Skin")

        # Charger les skins
        self.skin1 = Skin("graphics\character\idle/1.png")
        self.skin2 = Skin("graphics/character/idle/2.png")
        self.skin3 = Skin("graphics/character/idle/3.png")
        self.skin4 = Skin("graphics/character/idle/4.png")
        self.skin5 = Skin("graphics/character/idle/5.png")
        #self.skin6 = Skin("graphics/character/idle/6.png")

        # Sélection par défaut
        self.skin_actuel = self.skin1

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
                        if self.skin_actuel == self.skin1:
                            self.skin_actuel = self.skin2
                        else:
                            self.skin_actuel = self.skin1
                        
                        if self.skin_actuel == self.skin2:
                            self.skin_actuel = self.skin3
                        else:
                            self.skin_actuel = self.skin2
                        
                        if self.skin_actuel == self.skin3:
                            self.skin_actuel = self.skin4
                        else:
                            self.skin_actuel = self.skin3
                        
                        if self.skin_actuel == self.skin4:
                            self.skin_actuel = self.skin5
                        else:
                            self.skin_actuel = self.skin4
                        
                        if self.skin_actuel == self.skin5:
                            self.skin_actuel = self.skin1
                        else:
                            self.skin_actuel = self.skin5
                        '''
                        if self.skin_actuel == self.skin5:
                            self.skin_actuel = self.skin6
                        else:
                            self.skin_actuel = self.skin5
                        
                        if self.skin_actuel == self.skin6:
                            self.skin_actuel = self.skin1
                        else:
                            self.skin_actuel = self.skin6
                        '''
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