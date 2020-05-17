import pygame
import time


pygame.init()

size = width, height = 600, 800
bg_color = 0, 0, 0
white = (220, 220, 220)

screen = pygame.display.set_mode(size)


class Tetris():
	def __init__(self):
		self.cell_size = 30
		

	def draw_grid(self):
		c_size = self.cell_size

		# number of cells
		board_size = 10, 20
		x_size = board_size[0]
		y_size = board_size[1]

		# vertical lines
		for i in range(board_size[0] + 1):
			c = c_size * (i+1)
			pygame.draw.line(screen, white, (c, c_size), \
				(c , c_size*(y_size+1)), 1)
		# horizontal lines
		for j in range(board_size[1] + 1):
			c = c_size * (j+1)
			pygame.draw.line(screen, white, (c_size, c), \
				(c_size*(x_size+1), c), 1)
		




tetris = Tetris()
def main():
	run = True
	screen.fill(bg_color)
	while run:
		# clock.tick(60)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False
			if pygame.mouse.get_pressed()[0]:
				pass
		
			tetris.draw_grid()
		pygame.display.flip()

	pygame.quit()
	quit()


main()
