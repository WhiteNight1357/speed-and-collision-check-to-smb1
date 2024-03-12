import pygame
import player
import tile

pygame.init()

BLACK = (0, 0, 0)

pxsize = 2
size = [256 * pxsize, 240 * pxsize]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)
tile.load(pxsize)

pygame.display.set_caption("pysmb1")

campos = 0

clock = pygame.time.Clock()
end = False
debugging = False


def printtext(msg, color=BLACK, pos=(50, 50)):
    textsurface = font.render(msg, True, pygame.Color(color), None)
    textrect = textsurface.get_rect()
    textrect.topleft = pos

    screen.blit(textsurface, textrect)


mario = pygame.image.load("resource/player.png")
player = player.Player(left=pygame.K_a, right=pygame.K_d, up=pygame.K_w, down=pygame.K_s, a=pygame.K_k, b=pygame.K_j)
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
            if event.key == pygame.K_ESCAPE:
                end = True

    # get keyboard input
    keys = pygame.key.get_pressed()

    player.advance_frame(keys)

    while player.pxxpos - campos > 116:
        campos += 1

    player.collision_check(campos)

    # draw background
    screen.fill([227, 255, 250])
    tile.tile_draw("0x11", campos, screen, pxsize)

    # print debug info
    if debugging:
        printtext("pxxpos: " + str(player.pxxpos), BLACK, (50, 50))
        printtext("pxypos: " + str(player.pxypos), BLACK, (50, 70))
        printtext("hexxpos: " + player.hexxpos, BLACK, (50, 90))
        printtext("hexypos: " + player.hexypos, BLACK, (50, 110))
        printtext("hexxspeed: " + player.hexxspeed, BLACK, (50, 130))
        printtext("hexyspeed: " + player.hexyspeed, BLACK, (50, 150))
        printtext("oncampxxpos: " + str(player.pxxpos - campos), BLACK, (250, 50))

    # draw player
    screen.blit(mario, ((player.pxxpos - campos) * pxsize, player.pxypos * pxsize))

    pygame.display.flip()

pygame.quit()
exit(0)
