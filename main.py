import pygame
import player

pygame.init()

BLACK = (0, 0, 0)

pxsize = 2
size = [256 * pxsize, 240 * pxsize]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)

pygame.display.set_caption("pysmb1")

clock = pygame.time.Clock()
end = False
debugging = False


def printtext(msg, color=BLACK, pos=(50, 50)):
    textsurface = font.render(msg, True, pygame.Color(color), None)
    textrect = textsurface.get_rect()
    textrect.topleft = pos

    screen.blit(textsurface, textrect)


mario = pygame.image.load("resource/player.png")
player = player.Player()
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

    player.advance_frame(keys)

    # draw background
    screen.fill([227, 255, 250])

    # print debug info
    if debugging:
        printtext("pxxpos: " + str(player.pxxpos), 'BLACK', (50, 50))
        printtext("pxypos: " + str(player.pxypos), 'BLACK', (50, 70))
        printtext("hexxpos: " + player.hexxpos, 'BLACK', (50, 90))
        printtext("hexypos: " + player.hexypos, 'BLACK', (50, 110))
        printtext("hexxspeed: " + player.hexxspeed, 'BLACK', (50, 130))
        printtext("hexyspeed: " + player.hexyspeed, 'BLACK', (50, 150))

    # draw player
    screen.blit(mario, (player.pxxpos * pxsize, player.pxypos * pxsize))

    pygame.display.flip()

pygame.quit()
