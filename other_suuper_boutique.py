import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de certaines constantes
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Exemple de boutique dans un onglet')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 32)

# Création de la classe Boutique
class Boutique:
    def __init__(self):
        self.items_for_sale = [
            {"name": "Potion de soin", "price": 50},
            {"name": "Épée magique", "price": 100},
            {"name": "Armure robuste", "price": 150}
        ]
        self.inventory = []
        self.wallet = 500

    def show_shop(self):
        WINDOW.fill(WHITE)
        text_y = 50

        for item in self.items_for_sale:
            text = FONT.render(f"{item['name']} - {item['price']} pièces d'or", True, BLACK)
            WINDOW.blit(text, (50, text_y))
            text_y += 50

        text_y += 50
        for item in self.inventory:
            text = FONT.render(f"{item['name']}", True, BLACK)
            WINDOW.blit(text, (50, text_y))
            text_y += 50

        wallet_text = FONT.render(f"Porte-monnaie: {self.wallet} pièces d'or", True, BLACK)
        WINDOW.blit(wallet_text, (50, HEIGHT - 50))

    def action_boutique(self, mouse_x, mouse_y):
        index = (mouse_y - 50) // 50

        if 0 <= index < len(self.items_for_sale):
            selected_item = self.items_for_sale[index]

            if selected_item['price'] <= self.wallet:
                self.inventory.append(selected_item)
                self.wallet -= selected_item['price']

# Fonction pour exécuter la boutique dans un onglet distinct
def run_boutique():
    boutique = Boutique()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                boutique.action_boutique(mouse_x, mouse_y)

        boutique.show_shop()
        pygame.display.update()

    pygame.quit()
    sys.exit()

# Exemple d'utilisation en lançant la boutique dans un onglet séparé
run_boutique()
