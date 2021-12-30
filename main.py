import pygame

pygame.init()

BLACK = (0, 0, 0)

pxsize = 2
size = [256 * pxsize, 240 * pxsize]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)

pygame.display.set_caption("pysmb1")

clock = pygame.time.Clock()
end = False

player = pygame.image.load("resource/player.png")

size = 16 * pxsize
xpos = 0
ypos = 0
xspeed = 0
yspeed = 0
realxspeed = "0x0000"
realyspeed = "0x0000"
beforejumpxspeed = "0x0000"
ledgerunoffspeed = "0x0000"
pxxpos = 0
pxypos = 0
wallxstart = 0
wallystart = 400
wallxwidth = 512
wallywidth = 100
on_ground = False
debugging = False


def printtext(msg, color=BLACK, pos=(50, 50)):
    textsurface = font.render(msg, True, pygame.Color(color), None)
    textrect = textsurface.get_rect()
    textrect.topleft = pos

    screen.blit(textsurface, textrect)


def jump():
    global realxspeed
    global realyspeed
    global beforejumpxspeed
    global on_ground
    on_ground = False
    if abs(int(realxspeed, 16)) < int("0x1000", 16):
        realyspeed = "-0x4000"
        beforejumpxspeed = realxspeed
    elif int("0x1000", 16) <= abs(int(realxspeed, 16)) <= int("0x24ff", 16):
        realyspeed = "-0x4000"
        beforejumpxspeed = realxspeed
    elif int("0x2500") <= abs(int(realxspeed, 16)):
        realyspeed = "-0x5000"
        beforejumpxspeed = realxspeed


def y_psysics(holding_a):
    global realyspeed
    global beforejumpxspeed
    if int(realyspeed, 16) > 0 and holding_a:
        if abs(int(beforejumpxspeed, 16)) < int("0x1000", 16):
            realyspeed = hex(int(realyspeed, 16) + int("0x0200", 16))
        if int("0x1000", 16) <= abs(int(beforejumpxspeed, 16)) <= int("0x24ff", 16):
            realyspeed = hex(int(realyspeed, 16) + int("0x01e0", 16))
        if int("0x2500", 16) <= abs(int(beforejumpxspeed, 16)):
            realyspeed = hex(int(realyspeed, 16) + int("0x0280", 16))
    else:
        if abs(int(beforejumpxspeed, 16)) < int("0x1000", 16):
            realyspeed = hex(int(realyspeed, 16) + int("0x0700", 16))
        if int("0x1000", 16) <= abs(int(beforejumpxspeed, 16)) <= int("0x24ff", 16):
            realyspeed = hex(int(realyspeed, 16) + int("0x0600", 16))
        if int("0x2500", 16) <= abs(int(beforejumpxspeed, 16)):
            realyspeed = hex(int(realyspeed, 16) + int("0x0900", 16))


def fillnull(hexvalue):
    if len(hexvalue) == 3 and int(hexvalue, 16) > 0:
        hexvalue = hexvalue[:2] + "000" + hexvalue[2:]
    elif len(hexvalue) == 4 and int(hexvalue, 16) > 0:
        hexvalue = hexvalue[:2] + "00" + hexvalue[2:]
    elif len(hexvalue) == 5 and int(hexvalue, 16) > 0:
        hexvalue = hexvalue[:2] + "0" + hexvalue[2:]
    elif len(hexvalue) == 4 and int(hexvalue, 16) < 0:
        hexvalue = hexvalue[:3] + "000" + hexvalue[3:]
    elif len(hexvalue) == 5 and int(hexvalue, 16) < 0:
        hexvalue = hexvalue[:3] + "00" + hexvalue[3:]
    elif len(hexvalue) == 6 and int(hexvalue, 16) < 0:
        hexvalue = hexvalue[:3] + "0" + hexvalue[3:]
    elif int(hexvalue, 16) == 0:
        hexvalue = "0x0000"
    return hexvalue


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

    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        xspeed = 0
    elif keys[pygame.K_a] and keys[pygame.K_d]:
        xspeed = 0
    elif keys[pygame.K_a]:
        xspeed = -3
    elif keys[pygame.K_d]:
        xspeed = 3

    if keys[pygame.K_k] and on_ground:
        jump()
    if keys[pygame.K_k] and not on_ground:
        y_psysics(True)
    elif not keys[pygame.K_k] and not on_ground:
        y_psysics(False)

    if debugging and keys[pygame.K_r]:
        xpos = 0
        ypos = 0
        xspeed = 0
        yspeed = 0
        realxspeed = "0x0000"
        realyspeed = "0x0000"
        beforejumpxspeed = "0x0000"
        ledgerunoffspeed = "0x0000"
        on_ground = False

    # change value
    realxspeed = fillnull(realxspeed)
    realyspeed = fillnull(realyspeed)
    xspeed = int(realxspeed[0:-3], 16)
    yspeed = int(realyspeed[0:-3], 16)
    pxxpos = pxxpos + xspeed
    pxypos = pxypos + yspeed
    xpos = pxxpos * pxsize
    ypos = pxypos * pxsize

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
            on_ground = True
        if yspeed < 0:
            ypos = wallystart + wallywidth
            yspeed = 0

    # draw background
    screen.fill([227, 255, 250])

    # print debug info
    if debugging:
        printtext("xpos: " + str(xpos), 'BLACK', (50, 50))
        printtext("ypos: " + str(ypos), 'BLACK', (50, 70))
        printtext("xspeed: " + str(xspeed), 'BLACK', (50, 90))
        printtext("yspeed: " + str(yspeed), 'BLACK', (50, 110))

    # draw wall and player
    pygame.draw.rect(screen, [130, 130, 130], [wallxstart, wallystart, wallxwidth, wallywidth])
    screen.blit(player, (xpos, ypos))

    pygame.display.flip()

pygame.quit()
