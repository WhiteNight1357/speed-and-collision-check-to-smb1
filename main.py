import pygame

pygame.init()

BLACK = (0, 0, 0)

size = [400, 400]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)

pygame.display.set_caption("pysmb1")

clock = pygame.time.Clock()
end = False


def printtext(msg, color=BLACK, pos=(50, 50)):
    textsurface = font.render(msg, True, pygame.Color(color), None)
    textrect = textsurface.get_rect()
    textrect.topleft = pos

    screen.blit(textsurface, textrect)


player = pygame.image.load("resource/player.png")

size = 20
xpos = 0
ypos = 0
xspeed = 0
yspeed = 0
wallxstart = 150
wallystart = 150
wallxwidth = 100
wallywidth = 100
debugging = False

while not end:
    # set framerate
    clock.tick(60)

    # event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1 and not debugging:
                debugging = True
            elif event.key == pygame.K_F1 and debugging:
                debugging = False

    # get keyboard input
    keys = pygame.key.get_pressed()

    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        yspeed = 0
    elif keys[pygame.K_UP]:
        yspeed = -3
    elif keys[pygame.K_DOWN]:
        yspeed = 3
    else:
        yspeed = 0
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        xspeed = 0
    elif keys[pygame.K_LEFT]:
        xspeed = -3
    elif keys[pygame.K_RIGHT]:
        xspeed = 3
    else:
        xspeed = 0

    # draw background
    screen.fill([227, 255, 250])

    # change value
    xpos = xpos + xspeed
    ypos = ypos + yspeed

    # collision check
    if wallxstart - size < xpos < wallxstart + wallxwidth \
       and\
       wallystart - size < ypos < wallystart + wallywidth:
        if xspeed > 0:
            xpos = wallxstart - size
            xspeed = 0
        if xspeed < 0:
            xpos = wallxstart + wallxwidth
            xspeed = 0
        if yspeed > 0:
            ypos = wallystart - size
            yspeed = 0
        if yspeed < 0:
            ypos = wallystart + wallywidth
            yspeed = 0

    # print debug info
    if debugging:
        printtext("xpos: " + str(xpos), 'BLACK', (50, 50))
        printtext("ypos: " + str(ypos), 'BLACK', (50, 70))
        printtext("xspeed: " + str(xspeed), 'BLACK', (50, 90))
        printtext("yspeed: " + str(yspeed), 'BLACK', (50, 110))

    # draw wall and player
    # rect(on what, color, [xposition, yposition, xsize, ysize], line width:null to fill)
    pygame.draw.rect(screen, [130, 130, 130], [wallxstart, wallystart, wallxwidth, wallywidth])
    screen.blit(player, (xpos, ypos))

    pygame.display.flip()

pygame.quit()
