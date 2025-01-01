import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    pygame.font.init()

    return pygame.font.Font("assets/font.ttf", size)


class Game:
    def __init__(self):
        # Initialisation de votre jeu
        pass

    def run(self):
        # Logique principale de votre jeu
        pass



class Game:
	def __init__(self):

		# game attributes
		self.max_level = 5
		self.max_health = 100
		self.cur_health = 100
		self.__coins = 0
		self.xp = 0 

		# overworld creation
		self.overworld = Overworld(0,self.max_level,screen,self.create_level)
		self.status = 'overworld'

		# user interface 
		self.__ui = UI(screen)
	
	def get_xp(self):
		return(self.__xp)

	def get_ui(self):
		return(self.__ui)
	
	def get_coins(self):
		return(self.__coins)

	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_overworld,self.change_coins,self.change_health)
		self.status = 'level'

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'

	def change_coins(self,amount):
		self.__coins += amount

	def change_health(self,amount):
		self.cur_health += amount

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			if self.__coins >= 5:
				self.__coins -= 5
			else:
				self.__coins = 0
			self.max_level = 0
			self.overworld = Overworld(0,self.max_level,screen,self.create_level)
			self.status = 'overworld'
	
	#test perso
	def up(self):
		if self.__coins >= 5:
			self.xp += 1
			self.__coins = 0
			print(self.xp)
		
		if self.xp >= 5:
			self.max_health += 100
			self.cur_health += 150
			self.xp = 0
	

	def run(self):
		self.boutique = Boutique()
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			self.get_ui().show_health(self.cur_health,self.max_health)
			self.get_ui().show_coins(self.__coins)
			self.get_ui().show_xp()
			self.check_game_over()
			self.up()
			#self.boutique.run()
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_1]:
			self.boutique.run()
		



class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price



class Boutique:
    def __init__(self):
        self.__nom = 'Boutique'
        self.inventory = []

        self.items_for_sale = [
            Item("petite", 50),
            Item("moyenne", 100),
            Item("grd", 150),
            Item("A", 150),
            Item("Z", 150),
            Item("E", 150),
            Item("R", 150),
            Item("T", 150),
            Item("Y", 150),
            Item("D", 150),
            Item("G", 150),
            Item("H", 150),
            Item("I", 150),
            Item("J", 150),
            Item("K", 150),
            Item("l", 150),
            Item("M", 150),
            Item("P", 150),
        ]
        #self.HEIGHT = 11*64
        #self.WIDTH = 1200
        self.WINDOW = screen
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.FONT = pygame.font.Font(None, 32)
        self.game = Game()
        self.wallet = 500

    
    def get_nom_boutique(self):
        return self.__nom

    def show_shop(self):
        self.WINDOW.fill(self.WHITE)
        text_y = 50

        for item in self.items_for_sale:
            text = self.FONT.render(f"{item.name} - {item.price} pièces d'or", True, self.BLACK)
            self.WINDOW.blit(text, (50, text_y))
            text_y += 50

        text_y += 50
        for item in self.inventory:
            text = self.FONT.render(f"{item.name}", True, self.BLACK)
            self.WINDOW.blit(text, (50, text_y))
            text_y += 50

        wallet_text = self.FONT.render(f"Porte-monnaie: {self.wallet} pièces d'or", True, self.BLACK)
        self.WINDOW.blit(wallet_text, (50, self.screen_height - 50))

    def action_boutique(self, mouse_x, mouse_y):
        index = (mouse_y - 50) // 50

        if 0 <= index < len(self.items_for_sale):
            selected_item = self.items_for_sale[index]

            if selected_item['price'] <= self.wallet:
                self.inventory.append(selected_item)
                self.wallet -= selected_item['price']

    def run(self):
        self.show_shop()
        self.action_boutique()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill('grey')
	
	game.run()

	pygame.display.update()
	clock.tick(60)
