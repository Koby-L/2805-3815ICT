import pygame

from mk1settings import *
import random
class Environment():
    #This is the grid that the game is built upon


    def __init__(self):
        self.grid = [[0] * HorizontalNum for n in range(VerticalNum)]


    #Check to ensure that the point is on the grid
    def pointOnGrid( self,x, y ):
        return x>= 0 and y >=0 and x < VerticalNum and y < HorizontalNum
        
    #Make sure the point isn't a corner
    def pointNotCorner(self,px1, py1, px2, py2):
        return px1==px2 or py1==py2

        

    #Make sure it's a different point
    def EnsureDifferentPoint(self,px1, py1,px2,py2):
        return not(px1==px2 and py1==py2)

    #Look at the cells next to the point we're at (px,py) and see how many walls there are.

    def validNextCell(self,px,py):
        numNeighbouringWalls=0

        #Check in a 3x3 grid and count the walls we see.



        
        for y in range(py-1,py+2):
            for x in range(px-1,px+2):
                if self.pointOnGrid(x,y) :#Make sure the point is actaully on the grid (Avoid out indexing)
                    #Make sure that the point we're looking at is different and is a wall
                    if self.EnsureDifferentPoint(px,py,x,y) and self.grid[x][y]==1:
                        numNeighbouringWalls+=1
                        pass
        #Return boolean T/F (<3 neighouring walls and make sure the point we're at isn't a wall)
        #I should probably mention that this number of neighbouring walls can act as a sort of difficulty toggle. Increasing the cap will cause the generation of more walls. Decreasing it will reduce the generation of walls.
        return (numNeighbouringWalls<3) and self.grid[px][py]!=1

        
    #Once we've made the point we're looking at a wall we want to gather all of the neighbours of this new point and add those to the NodeStack in the generate maze function
    def findNeighbours(self,px,py):
        neighbours = []

        for y in range(py-1,py+2):
            for x in range(px-1,px+2):
                if self.pointOnGrid(x,y):
                    
                    if self.pointNotCorner(px,py,x,y) and self.EnsureDifferentPoint(px,py,x,y):
                        neighbours.append((x,y))


        return neighbours

    #Start with an empty grid and begin filling in walls.
    def generateMaze(self):
        NodeStack=[]
        
        #Top left corner
        NodeStack.append((0,0))

        while(len(NodeStack)>0):
            
           #Get the (x,y) co-ordinates from the end of the stack
            Cords=NodeStack[len(NodeStack)-1]

            NodeStack.pop()

            #
            if(self.validNextCell(Cords[0],Cords[1]) == True):
                self.grid[Cords[0]][Cords[1]]=1
                #Get all of the neighbours and then randomly add them to the stack
                neighbours=self.findNeighbours(Cords[0],Cords[1])
                NodeStack=self.RandomlyAdd(neighbours,NodeStack)
                



        #I was running out of time in the day to program this bit but essentially it's trying to make sure the maze has no
        #blocked off areas. I'm going to have to come back to this but it's not really important right now.
        for x in range(0,VerticalNum-2):
            for y in range(HorizontalNum-2):
                if self.grid[x-1][y]==1 and self.grid[x][y]==0 and self.grid[x+2][y] == 0 and self.grid[x+1][y]==1:
                    self.grid[x+1][y]=0
                if self.grid[x][y-1] == 0 and self.grid[x][y]==0 and self.grid[x][y+1]==1 and self.grid[x][y+2]==0:
                    self.grid[x][y+1]=0


        #Lock the floors and ceilings.
        for col in range(VerticalNum):
            self.grid[col][0]=1
            self.grid[col][HorizontalNum-1]=1
        
        for row in range(HorizontalNum):
            self.grid[0][row]=1
            self.grid[VerticalNum-1][row]=1
        return self.grid
        

    def RandomlyAdd(self,neighbours,NodeStack):
        #Where we're inserting the neighbour in the stack
        targetIndex=0

        
        while(len(neighbours) >0):
            #Get a random index
            targetIndex=random.randint(0,len(neighbours)-1)
            #Add a random neighbour onto the end of the stack
            NodeStack.append(neighbours[targetIndex])
            #Pop that neighbour
            neighbours.pop(targetIndex)

        return NodeStack

