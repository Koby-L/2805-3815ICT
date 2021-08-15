

class Ghost():



    def __init__(self):
        #The x and y are co-ordinates on the grid, not the location on the screen
        self.pos_x=5
        self.pos_y=5


        pass




    def findPacMan(self):

        pass


    def Death(self):


        pass



    #Ghost goes to pacman. It's just temporary movement, so I might come back to this.
    def TempMovement(self, pacx,pacy):
        if self.pos_x < pacx:

            self.pos_x += 0.25
            return
        elif self.pos_x > pacx:
            self.pos_x -=0.25
            return

        if self.pos_y < pacy:

            self.pos_y+=0.25
            return

        elif self.pos_y > pacy:

            self.pos_y-=0.25
            return


        pass