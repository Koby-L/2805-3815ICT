
import sys
from mk1settings import *
import pacman
import environment
import numpy
import ghosts
from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
pygame.init()

#SORT THIS INTO CLASSES LATER

WIDTH, HEIGHT = 448,576
SPRITEWIDTH,SPRITEHEIGHT = 16,16
FPS = 60
WHITE = (255,255,255)
PURPLE = (70,5,156)
BLACK = (0,0,0)
PLAYERSPEED = .5
font = pygame.font.SysFont(None,20)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_mode()
PAC_LOGO = pygame.image.load('pacLogo.png').convert_alpha()
PAC_LOGO = pygame.transform.scale(PAC_LOGO,(450,240))
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load('pacmanloop.wav')

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pac-Man")
canvas = pygame.Surface((WIDTH,HEIGHT))


def main_menu():
    looper = True
    
    playButton = pygame.Rect(20,300,200,50) #declaration

    quitButton = pygame.Rect(20,400,200,50) #declaration

    while (looper == True):
        #get the X and Y positions of the cursor
        mouseX,mouseY = pygame.mouse.get_pos()

        #check if there is a collision at the mouses X and Y coordinates
        if playButton.collidepoint((mouseX,mouseY)):
            if (click == True): # If the mouse has been clicked in the previous frame, activate following
                return
                pass

        if quitButton.collidepoint((mouseX,mouseY)):
            if (click == True): # If the mouse has been clicked in the previous frame, activate following
                pygame.quit()    
                sys.exit()
                pass                


        #reset the click so that collisions dont mess up        
        click = False

        WIN.fill((0,0,0))

        pygame.draw.rect(WIN,(255,0,0),playButton)
        draw_text('PLAY',font,(WHITE),WIN,20,300)

        pygame.draw.rect(WIN,(255,0,0),quitButton)
        draw_text('QUIT',font,(WHITE),WIN,20,400)

        WIN.blit(PAC_LOGO,(0,0))

        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if(event.key == K_ESCAPE):
                    looper = False
                    break
            if (event.type == MOUSEBUTTONDOWN):
                if event.button == 1:
                    click = True                            
        pygame.display.update()
        clock.tick(FPS)                   

def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

def draw_window(player,whatState,orientation):
    
        WIN.fill(BLACK)

        if(whatState <20):
            playerDisplay = PAC_STATE_1
        elif(whatState <40):
            playerDisplay = PAC_STATE_2
        else:
            playerDisplay = PAC_STATE_3


        if(orientation == 1):
            playerDisplay = pygame.transform.rotate(playerDisplay,90)
        elif(orientation == 2):
            playerDisplay = pygame.transform.rotate(playerDisplay,270)
        elif(orientation == 3):
            playerDisplay = pygame.transform.rotate(playerDisplay,180)

        playerDisplay
        WIN.blit(playerDisplay,(player.x,player.y))
        pygame.display.update()


class App:

    main_menu()

    def __init__(self):

        self.running_time=0
        pygame.init()

        #Set height and width
        self.screen = pygame.display.set_mode((width,height))

        #Set up clock
        self.clock=pygame.time.Clock()

        #Game is running
        self.running = True

        #Background/ This is jsut the directory my background is in. SO you could disable it or just replace it with your own image.
        self.bg = pygame.image.load("testbackground.jpg")

        #Sets up background image
        self.screen.blit(self.bg,(0,0))

        #The self.Env allows us to access any functions and members inside environment that we may need for the future.
        #So I want to leave it in until I know that we don't need any variables, just functions
        self.Env=environment.Environment()
        

        #Main game grid.
        self.grid = self.Env.generateMaze()

        #Creates our pacman information
        self.set_up_pac()


        self.Ghost1 = ghosts.Ghost()


    pygame.mixer.music.play(-1)    
    #Check input from keyboard
    def checkInput(self):

        #Check through the events
        for event in pygame.event.get():

            #Quit
            if event.type==pygame.QUIT:
                self.running= False

            
                #Down key, up key, right key and left key cases. See pacman.py for the definitions
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.pac.direction=2
                elif event.key==pygame.K_RIGHT:
                    self.pac.direction=1
                elif event.key==pygame.K_DOWN:
                    self.pac.direction=4
                elif event.key==pygame.K_UP:
                    self.pac.direction=3


    #Main game loop.
    def run(self):
        #Update for the start of the game
        pygame.display.update()

        #Main game loop.
        while self.running:

            


            #Check input from keyboard and change direction/quit
            self.checkInput()

            #Tick the clock
            self.clock.tick(fps)


            #Blit the screen
            self.grid = self.pac.PacMove(self.grid)
            self.Ghost1.TempMovement(self.pac.pos_x,self.pac.pos_y)
            self.screen.blit(self.bg,(0,0))
            self.DrawGrid()
            pygame.display.update()
                

        #When self.running is false we quit pygame and sys
        pygame.quit()
        sys.exit()


    #This is the grid that the game is built upon
    def DrawGrid(self):
        '''
        So, we don't have any sprites as of now. If you guys want sprites I'm happy to include them but in the planning i've done
        for how we can implement the random maze generation and ghost Aritficial Intelligence I found that the easiest method to do this
        was by keeping everything in the 2D array.



        Let me know what you think about the decision, I'm happy for the discussion
        
        

        Since we don't have any sprites the draw grid function is the main method for updating the screen, all it does is loop through
        The 2D array and draw things based on what is in the cell at the time (I.E Pacman, ghosts, pellets etc.)
        '''






        #Used in the double for loops
        x,y=0,0
        for row in self.grid:
            for col in row:
                #This condition can be changed for other conditions. It basically just decides what tile is a wall and what isn't.
                if col == 1:
                    rect=pygame.Rect(x,y,square,square)
                    pygame.draw.rect(self.screen,(255,0,0),rect,1)
                elif col==0:
                    rect=pygame.Rect(x,y,square,square)
                    pygame.draw.rect(self.screen,(255,255,255),rect,1)
                

                    #The self.pac.pos_y * square + half of square is just getting pacman's positions, translating it to the grid and then pushing
                    #pacman into the middle of the square. The last number at the end is the radius of the pacman circle.


                    #In the future when we add animated sprites we're probably going to have to get rid of this command and replace it
                    #with the image representing pacman's current state.

                
                pygame.draw.circle(self.screen,(255,255,0),(self.pac.pos_y*square + (square//2),self.pac.pos_x*square+(square//2)),15)
                pygame.draw.circle(self.screen,(255,192,203),(self.Ghost1.pos_y*square + (square//2),self.Ghost1.pos_x*square+(square//2)),15)




                #Increment the x value by the width of the rectangles
                x=x+square
            #After moving through the column we increment the y value by the width of the rectangles
            y=y+square

            #Reset the x position after moving down a column
            x=0
        

    
    #Create pacman and add him to a sprite group.
    def set_up_pac(self):

        #Even though he isn't a sprite, I'm going to leave this just in case he needs to become one.
        self.pac = pacman.Pac(7,7)
        self.pac_group = pygame.sprite.Group()
        self.pac_group.add(self.pac)



test = App()
test.DrawGrid()
test.run()
