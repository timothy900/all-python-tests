import pygame

win_width = 800
win_height = 600

pygame.display.set_caption('No internet')

#win = win = pygame.display.set_mode((win_width, win_height))

class Dino:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = pygame.Rect(x, y, 100, 200)

	def draw(self, win):
		win.blit(win, self.img)


def main():
	win = pygame.display.set_mode((win_width, win_height))
	dino = Dino(20,20)
	dino.draw(win)

	run = True
	while run:

		pygame.draw.polygon(win, (20,100,20), ((146, 0), (291, 106),(236, 277), (56, 277), (0, 106)))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

	pygame.quit()
	quit()


main()
