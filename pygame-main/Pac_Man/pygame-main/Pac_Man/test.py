import random
import os
import pygame as pg



# game constants
SCREENRECT = pg.Rect(0, 0, 640, 480)





##Planning##
#class Player():

#class Ghost():

#class Pellet():

#class PowerPellet():

#class Fruit():

#class Score():



def main(winstyle=0):
    # Initialize pygame
    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()
    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None
    fullscreen = False
    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)




# call the "main" function if running this script
if __name__ == "__main__":
    main()











