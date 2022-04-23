import pygame
from util import hexutil


class Player:

    def __init__(self):
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

    def x_physics(self, pressed_key):

        if self.on_ground:

            if pressed_key[pygame.K_d] and not pressed_key[pygame.K_a]:
                self.player_direction_is_right = True
                if int(self.hexxspeed, 16) >= 0:
                    if self.skidding:
                        self.skidding = False
                        if int(self.hexxspeed, 16) < int("0x0900", 16):
                            self.hexxspeed = "0x0900"
                    if pressed_key[pygame.K_j]:
                        self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x00e4")
                    else:
                        self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x0098")
                elif int(self.hexxspeed, 16) < 0:
                    self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x01a0")
                    self.skidding = True

            elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d]:
                self.player_direction_is_right = False
                if int(self.hexxspeed, 16) <= 0:
                    if self.skidding:
                        self.skidding = False
                        if int(self.hexxspeed, 16) > int("-0x0900", 16):
                            self.hexxspeed = "-0x0900"
                    if pressed_key[pygame.K_j]:
                        self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x00e4")
                    else:
                        self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x0098")
                elif int(self.hexxspeed, 16) > 0:
                    self.hexxspeed = hexutil.hexsub(self.hexxspeed, "0x01a0")
                    self.skidding = True

            if not pressed_key[pygame.K_a] and not pressed_key[pygame.K_d]:
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

            if abs(int(self.hexxspeed, 16)) < int("0x0130", 16):
                if pressed_key[pygame.K_d] and not pressed_key[pygame.K_a]:
                    self.hexxspeed = "0x0130"
                if pressed_key[pygame.K_a] and not pressed_key[pygame.K_d]:
                    self.hexxspeed = "-0x0130"

            if not pressed_key[pygame.K_j] and abs(int(self.hexxspeed, 16)) > int("0x1900", 16) and \
                    self.b_release_frames >= 10:
                if int(self.hexxspeed, 16) > 0:
                    self.hexxspeed = "0x1900"
                else:
                    self.hexxspeed = "-0x1900"
            elif pressed_key[pygame.K_j] and abs(int(self.hexxspeed, 16)) > int("0x2900", 16):
                if int(self.hexxspeed, 16) > 0:
                    self.hexxspeed = "0x2900"
                else:
                    self.hexxspeed = "-0x2900"

            if pressed_key[pygame.K_j]:
                self.b_release_frames = 0
            else:
                self.b_release_frames = self.b_release_frames + 1

        else:

            # pressing D, going forward
            if pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                    int(self.hexxspeed, 16) >= int("0x1900", 16) and self.player_direction_is_right:
                self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x00e4")
            elif pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                    int("0x0", 16) <= int(self.hexxspeed, 16) < int("0x1900", 16) and self.player_direction_is_right:
                self.hexxspeed = hexutil.hexadd(self.hexxspeed, "0x0098")

            # pressing A, going forward
            elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                    int(self.hexxspeed, 16) <= int("-0x1900", 16) and not self.player_direction_is_right:
                self.hexxspeed = hex(int(self.hexxspeed, 16) - int("0x00e4", 16))
            elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                    int("0x0", 16) > int(self.hexxspeed, 16) > int("-0x1900", 16) and \
                    not self.player_direction_is_right:
                self.hexxspeed = hex(int(self.hexxspeed, 16) - int("0x0098", 16))

            # pressing D, going backward
            elif pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                    int(self.hexxspeed, 16) <= int("-0x1900", 16) and not self.player_direction_is_right:
                self.hexxspeed = hex(int(self.hexxspeed, 16) + int("0x00e4", 16))
            elif pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                    int(self.hexxspeed, 16) > int("-0x1900", 16) and \
                    int(self.beforejumpxspeed, 16) <= int("-0x1d00", 16) and not self.player_direction_is_right:
                self.hexxspeed = hex(int(self.hexxspeed, 16) + int("0x00d0", 16))
            elif pressed_key[pygame.K_d] and not pressed_key[pygame.K_a] and \
                    int(self.hexxspeed, 16) > int("-0x1900", 16) and \
                    int(self.beforejumpxspeed, 16) > int("-0x1d00", 16) and not self.player_direction_is_right:
                self.hexxspeed = hex(int(self.hexxspeed, 16) + int("0x0098", 16))

            # pressing A, going backward
            elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                    int(self.hexxspeed, 16) >= int("0x1900", 16) and self.player_direction_is_right:
                self.hexxspeed = hex(int(self.hexxspeed, 16) - int("0x00e4", 16))
            elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                    int(self.hexxspeed, 16) < int("0x1900", 16) and \
                    int(self.beforejumpxspeed, 16) >= int("0x1d00", 16) and self.player_direction_is_right:
                self.hexxspeed = hex(int(self.hexxspeed, 16) - int("0x00d0", 16))
            elif pressed_key[pygame.K_a] and not pressed_key[pygame.K_d] and \
                    int(self.hexxspeed, 16) < int("0x1900", 16) and \
                    int(self.beforejumpxspeed, 16) < int("0x1d00", 16) and self.player_direction_is_right:
                self.hexxspeed = hex(int(self.hexxspeed, 16) - int("0x0098", 16))

            # walking speed cap & running speed cap
            if int(self.beforejumpxspeed, 16) >= int("-0x1900", 16) > int(self.hexxspeed, 16):
                self.hexxspeed = "-0x1900"
            elif int(self.beforejumpxspeed, 16) <= int("0x1900", 16) < int(self.hexxspeed, 16):
                self.hexxspeed = "0x1900"
            elif int(self.beforejumpxspeed, 16) < int("-0x1900", 16) and int(self.hexxspeed, 16) < int("-0x2900", 16):
                self.hexxspeed = "-0x2900"
            elif int(self.beforejumpxspeed, 16) > int("0x1900", 16) and int(self.hexxspeed, 16) > int("0x2900", 16):
                self.hexxspeed = "0x2900"

    def y_physics(self, pressed_key):

        if int(self.hexyspeed, 16) < 0 and pressed_key[pygame.K_a]:
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