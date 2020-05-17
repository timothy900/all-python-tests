import pygame
import time
import  math


size = width, height = 800, 600
display = pygame.display.set_mode(size)

player_img = pygame.image.load("player.png") # TEST LINE


class Player:

	def __init__(self):
		self.x = width/2
		self.y = height/2
		self.speed = 1
	
	def move(self):
		x, y = pygame.mouse.get_pos()
		print(x, y)
		x_distance = abs(x - self.x)
		y_distance = abs(y - self.y)
		self.x = math.floor(x_distance * self.speed)
		self.y = math.floor(y_distance * self.speed)
		
	def draw(self):
		print((self.x,self.y))
		display.blit(player_img, (self.x, self.y))


def main():
	player = Player()

	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False

		display.fill((30, 30, 90))

		player.move()
		player.draw()

		pygame.display.flip()
		#pygame.display.update()

	pygame.quit()
	quit()

main()
