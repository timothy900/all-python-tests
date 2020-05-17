import pygame

size = width, height = 800, 600
display = pygame.display.set_mode(size)

car_ = 

class Car:

	def __init__(self, vel):
		self.x = width
		self.vel = vel

	def move(self):
		self.x -= self.vel

	def draw(self):
		display.blit(car_, self.x, self.y)


class Bullet:

	def __init__(self):

