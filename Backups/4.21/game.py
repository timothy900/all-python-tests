import sys, pygame
import random
import time

pygame.init()

size = width, height = 800, 600
bg_color = 65, 65, 65

screen = pygame.display.set_mode(size)

player_sprite = pygame.image.load("player.png")
x = 75
player_height = player_sprite.get_size()[1]

box_sprite = pygame.image.load("box.png")

ground = pygame.image.load("ground.png")
ground_y = 100 # distance of ground from bottom of screen
ground_rect = (0, height - ground_y)

player_height = player_sprite.get_size()[1]


class Player:

	def __init__(self):
		self.y = 0
		#self.y = height - ground_y - player_height
		self.vel = 0
		self.coords = (x, self.y)
		self.tick_count = 0
		self.height = self.y
		self.jump_ = False

	def jump(self):
		#if self.y + player_height > ground_rect[1]:
		self.y -= 1
		self.tick_count = 0
		self.vel = -10.5
		#self.height = self.y

	def fall(self):
		self.tick_count += 1

		'''
		if self.y + player_height > ground_rect[1]: # if player is below ground
			self.y = ground_rect[1] + player_height # put player above ground
		else:
		'''
		d = self.vel*self.tick_count + 1.5*self.tick_count**2 # calculate fall

		if d >= 19:
			d = 19

		if d < 0:
			d -= 2
		self.y = self.y + d
		self.coords = (x, self.y)


	def draw(self):
		screen.blit(player_sprite, self.coords)

	def player_handler(self):
		if self.y + player_height < ground_rect[1]: # if player is above ground
			self.fall() # fall
		self.draw()



class Boxes:

	gap = 200

	def __init__(self):
		margin = 300 # how far off the screen the box spawns
		self.y = ground_rect[1] - box_sprite.get_size()[1]
		self.x = width + margin
		self.sprite = box_sprite

	def move(self):
		vel = 10
		self.x -= vel

	def draw(self):
		screen.blit(self.sprite, [self.x, self.y])


def box_init(num_boxes):
	boxes_list_ = []
	for i in range(num_boxes):
		boxes_list_.append(Boxes())
		boxes_list_[i].x = random.randint(0, 10)*(width/10)
	return boxes_list_

def draw_score(score_):
	None

def box_handler(boxes_list):
	score = 0
	for box in boxes_list:
		# when box past screen
		if box.x + box.sprite.get_size()[0] + 30 < 0:
			box.x = width + random.randint(0, 10)*(width/10)
		box.move()
		box.draw()

def main():
	box_ = box_init(2)
	player = Player()
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False
			if event.type == pygame.MOUSEBUTTONUP:
				player.jump()
				print("jumped")

		screen.fill(bg_color)

		player.player_handler()

		box_handler(box_)

		screen.blit(ground, ground_rect)
		pygame.display.flip()


	pygame.quit()
	quit()

main()
