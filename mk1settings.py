import pygame

#Grid settings, HoriztonalNum represents how many squares we want horiztonally. VerticalNum is how many squares we want vertically
HorizontalNum=20
VerticalNum = 15




#screen settings. Square is the size of the rectangles, this can be adjusted. Height and width of the screen is dependent on the size of the squares
square=40
width = HorizontalNum * square
height= VerticalNum * square
#We'll probably have to increase it by a static amount in order to get the score bar above the game

#Clock tick settings. Lower fps causes game to run slower, higher fps casues game to run faster
fps=10 