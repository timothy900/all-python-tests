import pygame
import math
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("yea")

bgColor = (0, 0, 0)

x = 50
y = 50
width = 60
height = 60
vel = 5

# magnet
box_x = 200
box_y = 450
box_w = 20
box_h = 20
box_center_x = box_x + (box_w/2)
box_center_y = box_y + (box_h/2)
box_color = (215, 0, 0)

run = True
while run:
    pygame.time.delay(33)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # refresh screen
    win.fill(bgColor)

    # draw red magnet
    pygame.draw.rect(win, box_color, (box_x, box_y, box_w, box_h))
    
    # make yellow box closer to red
    '''
    difference_x = box_center_x - x
    difference_y = box_center_y - y
    slope = difference_y/difference_x
    x = math.floor(x + 1)
    y = math.floor(x * slope)
    '''

    # draw yellow box
    pygame.draw.rect(win, (250, 212, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
