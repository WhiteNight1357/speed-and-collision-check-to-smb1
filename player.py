from mutil import hexutil


class Player:

    def __init__(self, left, right, up, down, a, b):
        self.pxxpos = 0
        self.pxypos = 0
        self.b_release_frames = 0
        self.hexxpos = "0x0000"
        self.hexypos = "0x0000"
        self.hexxspeed = "0x0000"
        self.hexyspeed = "0x0000"
        self.beforejumpxspeed = "0x0000"
        self.ledgerunoffspeed = "0x0000"
        self.on_ground = False
        self.a_already_pressed = False
        self.player_direction_is_right = True
        self.skidding = False
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.a = a
        self.b = b

    def x_physics(self, pressed_key):

        if self.on_ground:

            if pressed_key[self.right] and not pressed_key[self.left]:
                self.player_direction_is_right = True
                if int(self.hexxspeed, 16) >= 0:
                    if self.skidding:
                        self.skidding = False
                        if int(self.hexxspeed, 16) < int("0x0900", 16):
                            self.hexxspeed = "0x0900"
                    if pressed_key[self.b]:
                        self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x00e4")
                    else:
                        self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x0098")
                elif int(self.hexxspeed, 16) < 0:
                    self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x01a0")
                    self.skidding = True

            elif pressed_key[self.left] and not pressed_key[self.right]:
                self.player_direction_is_right = False
                if int(self.hexxspeed, 16) <= 0:
                    if self.skidding:
                        self.skidding = False
                        if int(self.hexxspeed, 16) > int("-0x0900", 16):
                            self.hexxspeed = "-0x0900"
                    if pressed_key[self.b]:
                        self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x00e4")
                    else:
                        self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x0098")
                elif int(self.hexxspeed, 16) > 0:
                    self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x01a0")
                    self.skidding = True

            if not pressed_key[self.left] and not pressed_key[self.right]:
                if not abs(int(self.hexxspeed, 16)) < int("0x0100", 16):
                    if self.skidding:
                        if int(self.hexxspeed, 16) > 0:
                            self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x01a0")
                        else:
                            self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x01a0")
                    else:
                        if int(self.hexxspeed, 16) > 0:
                            self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x00d0")
                        else:
                            self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x00d0")
            
            # minimum speed
            if abs(int(self.hexxspeed, 16)) < int("0x0130", 16):
                if pressed_key[self.right] and not pressed_key[self.left]:
                    self.hexxspeed = "0x0130"
                if pressed_key[self.left] and not pressed_key[self.right]:
                    self.hexxspeed = "-0x0130"

            # walking, running speed cap
            if not pressed_key[self.b] and abs(int(self.hexxspeed, 16)) > int("0x1900", 16) and \
                    self.b_release_frames >= 10:
                if int(self.hexxspeed, 16) > 0:
                    self.hexxspeed = "0x1900"
                else:
                    self.hexxspeed = "-0x1900"
            elif pressed_key[self.b] and abs(int(self.hexxspeed, 16)) > int("0x2900", 16):
                if int(self.hexxspeed, 16) > 0:
                    self.hexxspeed = "0x2900"
                else:
                    self.hexxspeed = "-0x2900"

        else:
            # air physics
            # pressing right, going forward
            if pressed_key[self.right] and not pressed_key[self.left] and \
                    int(self.hexxspeed, 16) > int("0x1900", 16) and self.player_direction_is_right:
                self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x00e4")
            elif pressed_key[self.right] and not pressed_key[self.left] and \
                    int(self.hexxspeed, 16) <= int("0x1900", 16) and self.player_direction_is_right:
                self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x0098")

            # pressing left, going forward
            elif pressed_key[self.left] and not pressed_key[self.right] and \
                    int(self.hexxspeed, 16) >=  int("-0x1900", 16) and not self.player_direction_is_right:
                self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x00e4")
            elif pressed_key[self.left] and not pressed_key[self.right] and \
                    int(self.hexxspeed, 16) < int("-0x1900", 16) and \
                    not self.player_direction_is_right:
                self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x0098")

            # pressing right, going backward
            elif pressed_key[self.right] and not pressed_key[self.left] and \
                    int(self.hexxspeed, 16) <= int("-0x1900", 16) and not self.player_direction_is_right:
                self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x00e4")
            elif pressed_key[self.right] and not pressed_key[self.left] and \
                    int(self.hexxspeed, 16) > int("-0x1900", 16) and \
                    int(self.beforejumpxspeed, 16) <= int("-0x1d00", 16) and not self.player_direction_is_right:
                self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x00d0")
            elif pressed_key[self.right] and not pressed_key[self.left] and \
                    int(self.hexxspeed, 16) > int("-0x1900", 16) and \
                    int(self.beforejumpxspeed, 16) > int("-0x1d00", 16) and not self.player_direction_is_right:
                self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x0098")

            # pressing left, going backward
            elif pressed_key[self.left] and not pressed_key[self.right] and \
                    int(self.hexxspeed, 16) >= int("0x1900", 16) and self.player_direction_is_right:
                self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x00e4")
            elif pressed_key[self.left] and not pressed_key[self.right] and \
                    int(self.hexxspeed, 16) < int("0x1900", 16) and \
                    int(self.beforejumpxspeed, 16) >= int("0x1d00", 16) and self.player_direction_is_right:
                self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x00d0")
            elif pressed_key[self.left] and not pressed_key[self.right] and \
                    int(self.hexxspeed, 16) < int("0x1900", 16) and \
                    int(self.beforejumpxspeed, 16) < int("0x1d00", 16) and self.player_direction_is_right:
                self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x0098")

            # walking speed cap & running speed cap
            if int(self.beforejumpxspeed, 16) >= int("-0x1900", 16) > int(self.hexxspeed, 16):
                self.hexxspeed = "-0x1900"
            elif int(self.beforejumpxspeed, 16) <= int("0x1900", 16) < int(self.hexxspeed, 16):
                self.hexxspeed = "0x1900"
            elif int(self.beforejumpxspeed, 16) < int("-0x1900", 16) and int(self.hexxspeed, 16) < int("-0x2900", 16):
                self.hexxspeed = "-0x2900"
            elif int(self.beforejumpxspeed, 16) > int("0x1900", 16) and int(self.hexxspeed, 16) > int("0x2900", 16):
                self.hexxspeed = "0x2900"

        if pressed_key[self.b]:
            self.b_release_frames = 0
        else:
            self.b_release_frames = self.b_release_frames + 1

    def y_physics(self, pressed_key):

        if int(self.hexyspeed, 16) < 0 and pressed_key[self.a]:
            if abs(int(self.beforejumpxspeed, 16)) < int("0x1000", 16):
                self.hexyspeed = hex(int(self.hexyspeed, 16) + int("0x0200", 16))
            if int("0x1000", 16) <= abs(int(self.beforejumpxspeed, 16)) <= int("0x24ff", 16):
                self.hexyspeed = hex(int(self.hexyspeed, 16) + int("0x01e0", 16))
            if int("0x2500", 16) <= abs(int(self.beforejumpxspeed, 16)):
                self.hexyspeed = hex(int(self.hexyspeed, 16) + int("0x0280", 16))
        else:
            if abs(int(self.beforejumpxspeed, 16)) < int("0x1000", 16):
                self.hexyspeed = hex(int(self.hexyspeed, 16) + int("0x0700", 16))
            if int("0x1000", 16) <= abs(int(self.beforejumpxspeed, 16)) <= int("0x24ff", 16):
                self.hexyspeed = hex(int(self.hexyspeed, 16) + int("0x0600", 16))
            if int("0x2500", 16) <= abs(int(self.beforejumpxspeed, 16)):
                self.hexyspeed = hex(int(self.hexyspeed, 16) + int("0x0900", 16))

        if int(self.hexyspeed, 16) > int("0x4800", 16):
            self.hexyspeed = "0x4000"

    def jump(self):

        self.on_ground = False
        if abs(int(self.hexxspeed, 16)) < int("0x1000", 16):
            self.hexyspeed = "-0x4000"
            self.beforejumpxspeed = self.hexxspeed
        elif int("0x1000", 16) <= abs(int(self.hexxspeed, 16)) <= int("0x24ff", 16):
            self.hexyspeed = "-0x4000"
            self.beforejumpxspeed = self.hexxspeed
        elif int("0x2500", 16) <= abs(int(self.hexxspeed, 16)):
            self.hexyspeed = "-0x5000"
            self.beforejumpxspeed = self.hexxspeed

    def advance_frame(self, pressed_keys):

        self.x_physics(pressed_keys)
        self.y_physics(pressed_keys)

        if pressed_keys[self.a] and self.on_ground and not self.a_already_pressed:
            self.jump()
            self.a_already_pressed = True

        if pressed_keys[self.a] and not self.on_ground:
            self.a_already_pressed = True
        elif not pressed_keys[self.a] and not self.on_ground:
            self.a_already_pressed = False
        elif not pressed_keys[self.a]:
            self.a_already_pressed = False

        # change value
        self.hexxspeed = hexutil.fillnull(self.hexxspeed)
        self.hexyspeed = hexutil.fillnull(self.hexyspeed)

        if not int(self.hexxspeed[0:-2], 16) == 0:
            self.hexxpos = hexutil.hexadd(self.hexxpos, self.hexxspeed)
        if not int(self.hexyspeed[0:-2], 16) == 0:
            self.hexypos = hexutil.hexadd(self.hexypos, self.hexyspeed)

        self.hexxpos = hexutil.fillnull(self.hexxpos)
        self.hexypos = hexutil.fillnull(self.hexypos)

        self.pxxpos = int(self.hexxpos[0:-3], 16)
        self.pxypos = int(self.hexypos[0:-3], 16)

    def collision_check(self, collisionrect, campos, pxsize):

        # reference: https://pbs.twimg.com/media/FGT7WjnVcAEBpBz?format=jpg&name=large
        oncamx = (self.pxxpos - campos) * pxsize
        oncamy = self.pxypos * pxsize

        # head check
        if int(self.hexyspeed, 16) <= 0 and \
                collisionrect.collidepoint(oncamx + 8 * pxsize, oncamy + 2 * pxsize):
            self.hexyspeed = "0x1" + self.hexyspeed[-3:]

        # foot check
        if int(self.hexyspeed, 16) >= 0 and \
                (collisionrect.collidepoint(oncamx + 3 * pxsize, oncamy + 16 * pxsize) or \
                collisionrect.collidepoint(oncamx + 12 * pxsize, oncamy + 16 * pxsize)):
            if oncamy % (16 * pxsize) <= 6:
                self.hexypos = self.hexypos[:-4] + "0" + self.hexypos[-3:]
                self.hexyspeed = "0x0000"
                self.on_ground = True
            else:
                if collisionrect.collidepoint(oncamx + 3 * pxsize, oncamy + 16 * pxsize) and \
                        not int(self.hexxspeed, 16) >= 0:
                    hexutil.hexadd(self.hexxpos, "0x1000")
                if collisionrect.collidepoint(oncamx + 12 * pxsize, oncamy + 16 * pxsize) and \
                        not int(self.hexxspeed, 16) <= 0:
                    hexutil.hexadd(self.hexxpos, "-0x1000")



        if self.pxypos > 180:
            self.hexyspeed = "0x0000"
            self.on_ground = True
            self.hexypos = "0xb4000"

        if self.pxxpos < campos:
            self.hexxspeed = "0x0000"
            self.hexxpos = hex(campos) + self.hexxpos[-3:]

        self.pxxpos = int(self.hexxpos[0:-3], 16)
        self.pxypos = int(self.hexypos[0:-3], 16)
