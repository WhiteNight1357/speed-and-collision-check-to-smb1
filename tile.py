import resources


def load(pxsize):
    resources.load(pxsize)


def tile_draw(level, campos, surface, pxsize):
    xpos = 0
    ypos = 0
    listxpos = 0
    listypos = 0
    collision_list = []

    if level == "0x11":
        level = resources.level1_1

    for row in level:
        for _ in row:
            tile = level[listypos][listxpos]
            if tile == 0 or xpos - campos < -16 * pxsize or xpos - campos > 256 * pxsize:
                xpos += 16
                listxpos += 1
                continue
            collision_list.append(surface.blit(resources.tileset[tile], ((xpos - campos) * pxsize, ypos * pxsize)))
            xpos += 16
            listxpos += 1
        ypos += 16
        xpos = 0
        listypos += 1
        listxpos = 0

    return collision_list
