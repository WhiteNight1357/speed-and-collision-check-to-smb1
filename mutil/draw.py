import pygame


# this function draws element of 'sprite' with color of 'palette'
# for example:
#    sprite = [[1, 0, 3, 2, 1, 2],
#              [2, 3, 0, 3, 1, 0]]
#    palette = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
#    draw(surface, xpos, ypos, pixelsize = 3, sprite, palette)
# will draw draw_example.png
def draw(surface, xpos, ypos, pixelsize, sprite, palette):

    x = xpos
    y = ypos

    for row in sprite:
        for item in row:

            if palette[item] is None:
                # draw transparent pixel (or don't draw the pixel)
                x += pixelsize
                continue
            pygame.draw.rect(surface, palette[item], [x, y, pixelsize, pixelsize])
            x += pixelsize

        x = xpos
        y += pixelsize