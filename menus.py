import pygame
import os
import sys
from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
pygame.init()

WIDTH, HEIGHT = 448,576
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pac-Man")
font = pygame.font.SysFont(None,20)
WHITE = (255,255,255)
YELLOW = (255,255,0)
FPS = 60
PAC_LOGO = pygame.image.load('pacLogo.png').convert_alpha()
PAC_LOGO = pygame.transform.scale(PAC_LOGO,(450,240))
MASCOT = pygame.image.load('mascot.png').convert_alpha()
MASCOT = pygame.transform.scale(MASCOT,(194,197))

clock = pygame.time.Clock()

def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

def configureMenu():
    conLooper = True
    conClick = False

    classicButton = pygame.Rect(20,200,200,50) #declaration
    randomButton = pygame.Rect(20,300,200,50) #declaration
    backButton = pygame.Rect(260,300,200,50) #declaration

    while(conLooper == True):
        #get the X and Y positions of the cursor
        mouseX,mouseY = pygame.mouse.get_pos()

        #check if there is a collision at the mouses X and Y coordinates
        if classicButton.collidepoint((mouseX,mouseY)):
            if (conClick == True): # If the mouse has been clicked in the previous frame, activate following\
                #ADD FUNCTIONALITY    
                return

        #check if there is a collision at the mouses X and Y coordinates
        if randomButton.collidepoint((mouseX,mouseY)):
            if (conClick == True): # If the mouse has been clicked in the previous frame, activate following
                #ADD FUNCTIONALITY    
                return


        #check if there is a collision at the mouses X and Y coordinates
        if backButton.collidepoint((mouseX,mouseY)):
            if (conClick == True): # If the mouse has been clicked in the previous frame, activate following
                conLooper = False

        click = False

        WIN.fill((0,0,0))
        pygame.draw.rect(WIN,(255,0,0),backButton)
        draw_text('BACK',font,(WHITE),WIN,20,200)    #For some reason this and classic isnt displaying? cant work out why right now

        pygame.draw.rect(WIN,(255,0,0),classicButton)
        draw_text('CLASSIC',font,(WHITE),WIN,20,300)

        pygame.draw.rect(WIN,(255,0,0),randomButton)
        draw_text('RANDOM',font,(WHITE),WIN,260,300)

        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if(event.key == K_ESCAPE):
                    conLooper = False
                    break
            if (event.type == MOUSEBUTTONDOWN):
                if event.button == 1:
                    conClick = True 

        pygame.display.update()
        clock.tick(FPS)      

def main_menu():
    
    looper = True
    
    playButton = pygame.Rect(20,200,200,50) #declaration

    configButton = pygame.Rect(20,300,200,50)

    quitButton = pygame.Rect(20,400,200,50) #declaration

    while (looper == True):
        #get the X and Y positions of the cursor
        mouseX,mouseY = pygame.mouse.get_pos()

        #check if there is a collision at the mouses X and Y coordinates
        if playButton.collidepoint((mouseX,mouseY)):
            if (click == True): # If the mouse has been clicked in the previous frame, activate following
                return
                pass

        if configButton.collidepoint((mouseX,mouseY)):
            if (click == True): # If the mouse has been clicked in the previous frame, activate following
                configureMenu()    
                     

        if quitButton.collidepoint((mouseX,mouseY)):
            if (click == True): # If the mouse has been clicked in the previous frame, activate following
                pygame.quit()    
                sys.exit()
                pass                


        #reset the click so that collisions dont mess up        
        click = False

        WIN.fill((0,0,0))

        pygame.draw.rect(WIN,(255,0,0),playButton)
        draw_text('PLAY',font,(WHITE),WIN,20,200)

        pygame.draw.rect(WIN,(255,0,0),configButton)
        draw_text('CONFIGURE',font,(WHITE),WIN,20,300)

        pygame.draw.rect(WIN,(255,0,0),quitButton)
        draw_text('QUIT',font,(WHITE),WIN,20,400)

        draw_text('By classes 2815/3815 of year 2021',font,(YELLOW),WIN,20,160)

        draw_text('Members:',font,(YELLOW),WIN,320,500)
        draw_text('Andrew Hamenko',font,(YELLOW),WIN,320,515)
        draw_text('Kathryn Hitchener',font,(YELLOW),WIN,320,530)
        draw_text('Koby Lestrelle',font,(YELLOW),WIN,320,545)
        draw_text('Leah Denny',font,(YELLOW),WIN,320,560)

        WIN.blit(PAC_LOGO,(0,0))

        WIN.blit(MASCOT,(240,240))

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

