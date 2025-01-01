import pygame

class UI:
	def __init__(self,surface):

		# setup 
		self.__display_surface = surface

		# health 
		self.health_bar = pygame.image.load('graphics/ui/health_bar.png').convert_alpha()
		self.health_bar_topleft = (54,39)
		self.bar_max_width = 152
		self.bar_height = 4

		# coins 
		self.coin = pygame.image.load('graphics/ui/coin.png').convert_alpha()
		self.coin_rect = self.coin.get_rect(topleft = (50,61))
		self.__font = pygame.font.Font('graphics/ui/ARCADEPI.ttf',30)

		# xp
		self.xpp = pygame.image.load('graphics/ui/xp.png').convert_alpha()

		self.xp_rect = self.xpp.get_rect(topleft = (70,61))
	
	def get_display_surface(self):
		return(self.__display_surface)

	def get_font(self):
		return(self.__font)

	def show_health(self,current,full):
		self.get_display_surface().blit(self.health_bar,(20,10))
		current_health_ratio = current / full
		current_bar_width = self.bar_max_width * current_health_ratio
		health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
		pygame.draw.rect(self.get_display_surface(),'#dc4949',health_bar_rect)

	def show_coins(self,amount):
		self.get_display_surface().blit(self.coin,self.coin_rect)
		coin_amount_surf = self.get_font().render(str(amount),False,'#33323d')
		coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right + 4,self.coin_rect.centery))
		self.get_display_surface().blit(coin_amount_surf,coin_amount_rect)
	
	def show_xp(self):
		self.get_display_surface().blit(self.xpp,(150,60))