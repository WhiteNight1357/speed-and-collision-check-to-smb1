# all smb1 player physics source:
# https://web.archive.org/web/20130807122227/http://i276.photobucket.com/albums/kk21/jdaster64/smb_playerphysics.png

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
pxxpos = 0
pxypos = 0
b_release_frames = 0
hexxspeed = "0x0000"
hexyspeed = "0x0000"
beforejumpxspeed = "0x0000"
ledgerunoffspeed = "0x0000"
hexxpos = "0x0000"
hexypos = "0x0000"
on_ground = False
a_already_pressed = False
player_direction_is_right = True
skidding = False
debugging = False


def printtext(msg, color=BLACK, pos=(50, 50)):
    textsurface = font.render(msg, True, pygame.Color(color), None)
    textrect = textsurface.get_rect()
    textrect.topleft = pos

    screen.blit(textsurface, textrect)


def jump():

    global hexxspeed
    global hexyspeed
    global beforejumpxspeed
    global on_ground

    on_ground = False
    if abs(int(hexxspeed, 16)) < int("0x1000", 16):
        hexyspeed = "-0x4000"
        beforejumpxspeed = hexxspeed
    elif int("0x1000", 16) <= abs(int(hexxspeed, 16)) <= int("0x24ff", 16):
        hexyspeed = "-0x4000"
        beforejumpxspeed = hexxspeed
    elif int("0x2500", 16) <= abs(int(hexxspeed, 16)):
        hexyspeed = "-0x5000"
        beforejumpxspeed = hexxspeed


def y_physics(holding_a):

    global hexyspeed
    global beforejumpxspeed

    if int(hexyspeed, 16) < 0 and holding_a:
        if abs(int(beforejumpxspeed, 16)) < int("0x1000", 16):
            hexyspeed = hex(int(hexyspeed, 16) + int("0x0200", 16))
        if int("0x1000", 16) <= abs(int(beforejumpxspeed, 16)) <= int("0x24ff", 16):
            hexyspeed = hex(int(hexyspeed, 16) + int("0x01e0", 16))
        if int("0x2500", 16) <= abs(int(beforejumpxspeed, 16)):
            hexyspeed = hex(int(hexyspeed, 16) + int("0x0280", 16))
    else:
        if abs(int(beforejumpxspeed, 16)) < int("0x1000", 16):
            hexyspeed = hex(int(hexyspeed, 16) + int("0x0700", 16))
        if int("0x1000", 16) <= abs(int(beforejumpxspeed, 16)) <= int("0x24ff", 16):
            hexyspeed = hex(int(hexyspeed, 16) + int("0x0600", 16))
        if int("0x2500", 16) <= abs(int(beforejumpxspeed, 16)):
            hexyspeed = hex(int(hexyspeed, 16) + int("0x0900", 16))

    if int(hexyspeed, 16) > int("0x4800", 16):
        hexyspeed = "0x4000"


def x_physics(pressed_key, in_air):

    global hexxspeed
    global beforejumpxspeed
    global player_direction_is_right
    global b_release_frames
    global skidding

    if not in_air:

        if pressed_key[pygame.K_d] and not pressed_key[pygame.K_a]:
            player_direction_is_right = True
            if int(hexxspeed, 16) >= 0:
                if skidding:
                    skidding = False
                    if int(hexxspeed, 16) < int("0x0900", 16):
                        hexxspeed = "0x0900"
                if pressed_key[pygame.K_j]:
                    hexxspeed = hex(int(hexxspeed, 16) + int("0x00e4", 16))
                else:
                    hexxspeed = hex(int(hexxspeed, 16) + int("0x0098", 16))
            elif int(hexxspeed, 16) < 0:
                hexxspeed = hex(int(hexxspeed, 16) + int("0x01a0", 16))
                skidding = True

        elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d]:
            player_direction_is_right = False
            if int(hexxspeed, 16) <= 0:
                if skidding:
                    skidding = False
                    if int(hexxspeed, 16) > int("-0x0900", 16):
                        hexxspeed = "-0x0900"
                if pressed_key[pygame.K_j]:
                    hexxspeed = hex(int(hexxspeed, 16) - int("0x00e4", 16))
                else:
                    hexxspeed = hex(int(hexxspeed, 16) - int("0x0098", 16))
            elif int(hexxspeed, 16) > 0:
                hexxspeed = hex(int(hexxspeed, 16) - int("0x01a0", 16))
                skidding = True

        if not pressed_key[pygame.K_a] and not pressed_key[pygame.K_d]:
            if not abs(int(hexxspeed, 16)) < int("0x0100", 16):
                if skidding:
                    if int(hexxspeed, 16) > 0:
                        hexxspeed = hex(int(hexxspeed, 16) - int("0x01a0", 16))
                    else:
                        hexxspeed = hex(int(hexxspeed, 16) + int("0x01a0", 16))
                else:
                    if int(hexxspeed, 16) > 0:
                        hexxspeed = hex(int(hexxspeed, 16) - int("0x00d0", 16))
                    else:
                        hexxspeed = hex(int(hexxspeed, 16) + int("0x00d0", 16))

        if abs(int(hexxspeed, 16)) < int("0x0130", 16):
            if pressed_key[pygame.K_d] and not pressed_key[pygame.K_a]:
                hexxspeed = "0x0130"
            if pressed_key[pygame.K_a] and not pressed_key[pygame.K_d]:
                hexxspeed = "-0x0130"

        if not pressed_key[pygame.K_j] and abs(int(hexxspeed, 16)) > int("0x1900", 16) and b_release_frames >= 10:
            if int(hexxspeed, 16) > 0:
                hexxspeed = "0x1900"
            else:
                hexxspeed = "-0x1900"
        elif pressed_key[pygame.K_j] and abs(int(hexxspeed, 16)) > int("0x2900", 16):
            if int(hexxspeed, 16) > 0:
                hexxspeed = "0x2900"
            else:
                hexxspeed = "-0x2900"

        if pressed_key[pygame.K_j]:
            b_release_frames = 0
        else:
            b_release_frames = b_release_frames + 1

    if in_air:

        # pressing D, going forward
        if pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                int(hexxspeed, 16) >= int("0x1900", 16) and player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) + int("0x00e4", 16))
        elif pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                int("0x0", 16) <= int(hexxspeed, 16) < int("0x1900", 16) and player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) + int("0x0098", 16))

        # pressing A, going forward
        elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                int(hexxspeed, 16) <= int("-0x1900", 16) and not player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) - int("0x00e4", 16))
        elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                int("0x0", 16) > int(hexxspeed, 16) > int("-0x1900", 16) and not player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) - int("0x0098", 16))

        # pressing D, going backward
        elif pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                int(hexxspeed, 16) <= int("-0x1900", 16) and not player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) + int("0x00e4", 16))
        elif pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                int(hexxspeed, 16) > int("-0x1900", 16) and int(beforejumpxspeed, 16) <= int("-0x1d00", 16) and \
                not player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) + int("0x00d0", 16))
        elif pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                int(hexxspeed, 16) > int("-0x1900", 16) and int(beforejumpxspeed, 16) > int("-0x1d00", 16) and \
                not player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) + int("0x0098", 16))

        # pressing A, going backward
        elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                int(hexxspeed, 16) >= int("0x1900", 16) and player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) - int("0x00e4", 16))
        elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                int(hexxspeed, 16) < int("0x1900", 16) and int(beforejumpxspeed, 16) >= int("0x1d00", 16) and \
                player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) - int("0x00d0", 16))
        elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                int(hexxspeed, 16) < int("0x1900", 16) and int(beforejumpxspeed, 16) < int("0x1d00", 16) and \
                player_direction_is_right:
            hexxspeed = hex(int(hexxspeed, 16) - int("0x0098", 16))

        # walking speed cap & running speed cap
        if int(beforejumpxspeed, 16) >= int("-0x1900", 16) > int(hexxspeed, 16):
            hexxspeed = "-0x1900"
        elif int(beforejumpxspeed, 16) <= int("0x1900", 16) < int(hexxspeed, 16):
            hexxspeed = "0x1900"
        elif int(beforejumpxspeed, 16) < int("-0x1900", 16) and int(hexxspeed, 16) < int("-0x2900", 16):
            hexxspeed = "-0x2900"
        elif int(beforejumpxspeed, 16) > int("0x1900", 16) and int(hexxspeed, 16) > int("0x2900", 16):
            hexxspeed = "0x2900"


# fill meaningless 0s in hexvalue (used for slicing)
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

    x_physics(keys, not on_ground)

    if keys[pygame.K_k] and on_ground and not a_already_pressed:
        jump()
        a_already_pressed = True
    if keys[pygame.K_k] and not on_ground:
        y_physics(True)
        a_already_pressed = True
    elif not keys[pygame.K_k] and not on_ground:
        y_physics(False)
        a_already_pressed = False
    elif not keys[pygame.K_k]:
        a_already_pressed = False

    if debugging and keys[pygame.K_r]:
        xpos = 0
        ypos = 0
        xspeed = 0
        yspeed = 0
        hexxspeed = "0x0000"
        hexyspeed = "0x0000"
        beforejumpxspeed = "0x0000"
        ledgerunoffspeed = "0x0000"
        on_ground = False

    # change value
    hexxspeed = fillnull(hexxspeed)
    hexyspeed = fillnull(hexyspeed)

    if not int(hexxspeed[0:-2], 16) == 0:
        hexxpos = hex(int(hexxpos, 16) + int(hexxspeed, 16))
    if not int(hexyspeed[0:-2], 16) == 0:
        hexypos = hex(int(hexypos, 16) + int(hexyspeed, 16))

    hexxpos = fillnull(hexxpos)
    hexypos = fillnull(hexypos)

    pxxpos = int(hexxpos[0:-3], 16)
    pxypos = int(hexypos[0:-3], 16)

    if pxypos > 180:   # future collision check /w tiles will go here
        hexyspeed = "0x0000"
        on_ground = True
        pxypos = 180
        hexypos = "0xb4000"

    xpos = pxxpos * pxsize
    ypos = pxypos * pxsize

    # collision check
#    if wallxstart - size < xpos < wallxstart + wallxwidth \
#       and\
#       wallystart - size < ypos < wallystart + wallywidth:
#        if xspeed > 0:
#            xpos = wallxstart - size
#            xspeed = 0
#        if xspeed < 0:
#            xpos = wallxstart + wallxwidth
#            xspeed = 0
#        if yspeed > 0:
#            ypos = wallystart - size
#            yspeed = 0
#            on_ground = True
#        if yspeed < 0:
#            ypos = wallystart + wallywidth
#            yspeed = 0

    # draw background
    screen.fill([227, 255, 250])

    # print debug info
    if debugging:
        printtext("pxxpos: " + str(pxxpos), 'BLACK', (50, 50))
        printtext("pxypos: " + str(pxypos), 'BLACK', (50, 70))
        printtext("hexxpos: " + hexxpos, 'BLACK', (50, 90))
        printtext("hexypos: " + hexypos, 'BLACK', (50, 110))
        printtext("hexxspeed: " + hexxspeed, 'BLACK', (50, 130))
        printtext("hexyspeed: " + hexyspeed, 'BLACK', (50, 150))

    # draw player
    screen.blit(player, (xpos, ypos))

    pygame.display.flip()

pygame.quit()
