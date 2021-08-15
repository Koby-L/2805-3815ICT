import pygame
import os
import sys
# from pygame import font
from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
pygame.init()

##########

#VARIABLERS AND STUFF
WIDTH, HEIGHT = 448,576
SPRITEWIDTH,SPRITEHEIGHT = 16,16
FPS = 60
WHITE = (255,255,255)
PURPLE = (70,5,156)
BLACK = (0,0,0)
PLAYERSPEED = .5

font = pygame.font.SysFont(None,20)

#LOAD FROM PATH
# pygame.image.load(os.path.join('pacman testing','pac01.png'))


#PULL SPRITES
PAC_STATE_1 = pygame.image.load('pac01.png')
PAC_STATE_1 = pygame.transform.scale(PAC_STATE_1,(SPRITEWIDTH,SPRITEHEIGHT))
PAC_STATE_2 = pygame.image.load('pac02.png')
PAC_STATE_2 = pygame.transform.scale(PAC_STATE_2,(SPRITEWIDTH,SPRITEHEIGHT))
PAC_STATE_3 = pygame.image.load('pac03.png')
PAC_STATE_3 = pygame.transform.scale(PAC_STATE_3,(SPRITEWIDTH,SPRITEHEIGHT))


#menu items

pygame.display.set_mode()
PAC_LOGO = pygame.image.load('pacLogo.png').convert_alpha()
PAC_LOGO = pygame.transform.scale(PAC_LOGO,(450,240))


clock = pygame.time.Clock()


#SPEED OF GAME ANIMATIONS
animspeed = 6


#WINDOW SETTINGS
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pac-Man")
canvas = pygame.Surface((WIDTH,HEIGHT))


#PULL AUDIO
pygame.mixer.init()
#macman sound as music????
# pacloop = pygame.mixer.Sound('pacmanloop.wav')
pygame.mixer.music.load('pacmanloop.wav')



#FUNCTION THAT RENDERS THE GAME
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

def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

click = False   #initialise click to false

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


def main():
    #SETUP
    player = pygame.Rect(100,300,SPRITEWIDTH,SPRITEHEIGHT) #change this .x and .y to change position

    stateManager = 0
    stateIncrement = True
    orientation = 0


    run = True

    main_menu()

    pygame.mixer.music.play(-1)
    #MAIN LOOP BELOW
    while run:
        clock.tick(FPS)

        if (stateManager >= 60 and stateIncrement == True):
            stateIncrement = False
        if (stateManager <= 0 and stateIncrement == False):
            stateIncrement = True

        if (stateIncrement == True):
            stateManager+=animspeed
        else:
            stateManager-=animspeed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]: #up
            orientation = 1          
        elif keys_pressed[pygame.K_s]: #down  
            orientation = 2        
        elif keys_pressed[pygame.K_a]: #left
            orientation = 3
        elif keys_pressed[pygame.K_d]: #right 
            orientation = 4 

        if orientation == 1:
            player.y -= 1
        elif orientation == 2:
            player.y += 1
        elif orientation == 3:
            player.x -= 1
        else:
            player.x += 1

        draw_window(player,stateManager,orientation)



    pygame.quit


#RUN    
if __name__ == "__main__":
    main()