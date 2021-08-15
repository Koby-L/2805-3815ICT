from numpy import absolute

import math

from mk1settings import *
#Even though he technically isn't a sprite I'm leaving the code like this just incase we need to make him one.
class Pac (pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):

        super().__init__()
        self.pos_x = pos_x
        self.pos_y=pos_y
        self.direction=1
        #1=RIGHT;2=LEFT;3=UP;4=DOWN

    def PacMove(self,grid):
        #Moves the pacman sprite through the grid



        '''
        The thing about the PacMove is that I had to modify it to allow pacman to move slowly over the screen since the main
        method of keeping track in everything is mk1main.py grid variable.

        In order to do this I based the printing of pacman's location off of his pos_x and pos_y co-ordinates. But then I needed a method to ensure
        That he was still in a grid tile (So he could eat pellets etc.) In order to do this I used math.ceil and math.floor libraries
        to extend his movement into 4 separate frames.


        So if we wanted pacmain to move from grid [11][7] to grid [12][7] we can change it from a single leap (11 -> 12)
        into a 5 part leap (11 -> 11.25 -> 11.50 -> 11.75 -> 12)

        In order to make sure we could still account for the positioning of walls the math.ceil funciton was used.
        e.g. If grid [12][7] contained a wall we can check array index math.ceil(11+0.25) which is the value 12 and see that there is a wall.

        The movement isn't perfected, but I think it's a good start.
        
        I should also stress that the teleportation (tunnels on the left and right edges of the screen) hasn't been implemented. So going to those
        will probably make the game crash from indexing out of list range
        '''


        #I should also mention that those pairs of commented out lines actually had pacman existing in the amze but I've decided to take it out for now, 
        #Leaving the lines just in case we need to use those in the future.



        #Direction 4 is down
        if self.direction==4:
            
            if grid[math.ceil(self.pos_x+0.25)][math.floor(self.pos_y)] == 1:
                pass
            else:
                #grid[math.floor(self.pos_x)][math.floor(self.pos_y)]=0
                #grid[math.ceil(self.pos_x+0.25)][math.floor(self.pos_y)] = 3
                self.pos_x +=0.25
        elif self.direction==3:
            if grid[math.floor(self.pos_x-0.25)][math.floor(self.pos_y)]==1:
                pass
            else:
                #grid[math.ceil(self.pos_x)][math.floor(self.pos_y)]=0
                #grid[math.floor(self.pos_x-0.25)][math.floor(self.pos_y)] = 3
                self.pos_x-=0.25

        elif self.direction ==2:
            if grid[math.floor(self.pos_x)][math.floor(self.pos_y-0.25)] == 1:
                pass
            else:
                #grid[math.floor(self.pos_x)][math.ceil(self.pos_y)]=0
                #grid[math.floor(self.pos_x)][math.floor(self.pos_y-0.25)] = 3
                self.pos_y-=0.25


        elif self.direction==1:
            if grid[math.floor(self.pos_x)][math.ceil(self.pos_y+0.25)] == 1:
                pass
            else:
                #grid[math.floor(self.pos_x)][math.floor(self.pos_y)]=0
                #grid[math.floor(self.pos_x)][math.ceil(self.pos_y+0.25)]=3
                self.pos_y +=0.25

        return grid
        
        

        