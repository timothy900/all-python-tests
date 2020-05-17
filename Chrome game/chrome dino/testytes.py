'''
Chrome No-internet dinosaur game
'''

import pygame
import os

#pygame.init()

win_width = 500
win_height = 500
	
player_color = (40, 80, 200)# RGB
bg_color = (150, 150, 150)

win = pygame.display.set_mode((win_width, win_height))

dino_img = pygame.transform.scale2x(pygame.image.load(os.path.join("player2.png")))

# player
class Dino:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.tick_count = 0
		self.vel = 0
		self.height = self.y
		self.img = dino_img

	def jump(self):
		self.vel = -10.5
		self.tick_count = 0
		self.height = self.y

	def move(self):
		self.tick_count += 1

		# d is displacement in y axis
		#if not self.y > ground_y:
		d = self.vel*self.tick_count + 1.5*self.tick_count**2###### 

		# terminal velocity
		if d >= 16:
			d = 16

		if d < 0:
			d -= 2

		self.y = self.y + d

	def draw(self, win):
		rect = self.img.get_rect(center=self.img.get_rect(topleft=(self.x,self.y)).center)
		win.blit(self.img)

def draw_window(win, dino):
	win.fill(bg_color)
	dino.draw(win)
	pygame.display.update()

'''
# obstacle
class Cacti:
'''

def main():
	dino = Dino(100,100)
	win = pygame.display.set_mode((win_width, win_height))

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		draw_window(win, dino)

	pygame.quit()
	quit()


main()
