import pygame

pygame.init()

BLACK = (0, 0, 0)

size = [400, 400]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("asdf", 20)

pygame.display.set_caption("Quadstep simulaion")

clock = pygame.time.Clock()
end = False

xpos = 250
ypos = 250
xspeed = 5
yspeed = 5


def printtext(msg, color=BLACK, pos=(50, 50)):
    textSurface = font.render(msg, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos

    screen.blit(textSurface, textRect)

while end == False:
    clock.tick(30)

#    if end == True:
#        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    screen.fill([227, 255, 250])

    printtext("xpos: " + str(xpos))
    printtext("ypos: " + str(ypos), 'BLACK', (50, 70))
    printtext("xspeed: " + str(xspeed), 'BLACK', (50, 90))
    printtext("yspeed: " + str(yspeed), 'BLACK', (50, 110))

#    rect(on what, color, [xposition, yposition, xsize, ysize], line width:null to fill)
    pygame.draw.rect(screen, [0, 0, 0], [xpos, ypos, 20, 20], 1)

    xpos = xpos + xspeed
    ypos = ypos + yspeed
    xspeed = xspeed - 0.5
    yspeed = yspeed - 0.5

    if xpos < 0 and ypos < 0:
        end = True

    pygame.display.flip()

pygame.quit()