import pygame
import sys


pygame.init()



class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

inventory = []


items_for_sale = [
    Item("Potion de soin", 50),
    Item("Épée magique", 100),
    Item("Armure robuste", 150)
]


class Boutique:
    def __init__(self):
        self.__nom = 'Boutique'
        self.WIDTH, self.HEIGHT = 800, 600
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Boutique d\'objets')

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.FONT = pygame.font.Font(None, 32)
        self.wallet = 100  # Porte-monnaie initial du joueur
    
    def get_nom_boutique(self):
        return(self.__nom)

    def show_shop(self):
        self.WINDOW.fill(self.WHITE)
        text_y = 50

        for item in items_for_sale:
            text = self.FONT.render(f"{item.name} - {item.price} pièces d'or", True, self.BLACK)
            self.WINDOW.blit(text, (50, text_y))
            #text_y += 50

        text_y += 50
        for item in inventory:
            text = self.FONT.render(f"{item.name}", True, self.BLACK)
            self.WINDOW.blit(text, (50, text_y))
            text_y += 50

        wallet_text = self.FONT.render(f"Porte-monnaie: {self.wallet} pièces d'or", True, self.BLACK)
        self.WINDOW.blit(wallet_text, (50, self.HEIGHT - 50))
    
    def action_boutique(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            self.index = (self.mouse_y - 50) // 50

            if 0 <= self.index < len(items_for_sale):
                selected_item = items_for_sale[self.index]

                if selected_item.price <= self.wallet:  # Vérification si le joueur a assez d'argent
                    inventory.append(selected_item)
                    self.wallet -= selected_item.price  # Déduction du prix de l'objet du porte-monnaie du joueur

    def run(self):
        self.show_shop()
        self.action_boutique()

boutique = Boutique()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        boutique.run()
    pygame.display.update()

pygame.quit()
sys.exit()