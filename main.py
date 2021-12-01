import pygame

pygame.init()

BLACK = (0, 0, 0)

size = [400, 400]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)

pygame.display.set_caption("Quadstep simulaion")

clock = pygame.time.Clock()
end = False
frame = 0


def printtext(msg, color=BLACK, pos=(50, 50)):
    textsurface = font.render(msg, True, pygame.Color(color), None)
    textrect = textsurface.get_rect()
    textrect.topleft = pos

    screen.blit(textsurface, textrect)


screen.fill([227, 255, 250])
printtext("Check Python Prompt First")
pygame.display.flip()

selected_frame = int(input("process until frame#: "))
xpos = float(input("start x position: "))
ypos = float(input("start y position: "))
xspeed = float(input("start xspeed value: "))
yspeed = float(input("start yspeed value: "))
xspeedchange = float(input("xspeed change per frame value: "))
yspeedchange = float(input("yspeed change per frame value: "))

while end == False:
    clock.tick(30)

#    if end == True:
#        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    screen.fill([227, 255, 250])

    printtext("frame: " + str(frame), 'BLACK', (50, 30))
    printtext("xpos: " + str(xpos), 'BLACK', (50, 50))
    printtext("ypos: " + str(ypos), 'BLACK', (50, 70))
    printtext("xspeed: " + str(xspeed), 'BLACK', (50, 90))
    printtext("yspeed: " + str(yspeed), 'BLACK', (50, 110))

#    rect(on what, color, [xposition, yposition, xsize, ysize], line width:null to fill)
    pygame.draw.rect(screen, [0, 0, 0], [xpos, ypos, 20, 20], 1)

    xpos = xpos + xspeed
    ypos = ypos + yspeed
    xspeed = xspeed + xspeedchange
    yspeed = yspeed + yspeedchange

    if frame == selected_frame:
        end = True
    else:
        frame = frame + 1

    pygame.display.flip()

pygame.quit()