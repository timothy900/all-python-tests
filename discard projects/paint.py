import pygame
from pygame import gfxdraw


pygame.init()

size = width, height = 600, 800
bg_color = 20, 20, 20
white = (220, 220, 220)

screen = pygame.display.set_mode(size)


def paint(mouse_pos):
	pixArray = pygame.PixelArray(screen)
	pixArray[mouse_pos[0]][mouse_pos[1]] = white

	r = 9
	
	pygame.gfxdraw.filled_circle(screen, mouse_pos[0],mouse_pos[1], \
		r, white)


def main():
	run = True
	screen.fill(bg_color)
	clock = pygame.time.Clock()
	while run:
		clock.tick(60)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False
			if pygame.mouse.get_pressed()[0]:
				try:
					paint(event.pos)
					print(event.pos)
				except AttributeError:
					pass

		

		pygame.display.flip()

	pygame.quit()
	quit()


main()
