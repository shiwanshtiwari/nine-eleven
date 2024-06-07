from email.mime import base
import random
import sys 
import pygame
from pygame.locals import *
FPS =32
SCREENWIDTH=589
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT)) 
GROUNDY= SCREENHEIGHT * 0.8
GAME_SPRITES={}
GAME_SOUNDS={} 
PLAYER ='911 game/allah/airplane.webp'
BACKGROUND = '911 game/allah/images.jpg'
BUILDING = '911 game/allah/building.png.jpg'

def welcomescreen():

    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    zx = int((SCREENWIDTH - GAME_SPRITES['z'].get_width())/2)
    zy = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
             if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
             elif event.type == KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                 return 
             else: SCREEN.blit
             (GAME_SPRITES['background'], (0, 0))  

        SCREEN.blit (GAME_SPRITES['player'], (playerx, playery))    
        SCREEN.blit(GAME_SPRITES['z'],(zx,zy ))    
        SCREEN.blit(GAME_SPRITES['base'],(base, GROUNDY))    
        pygame.display.update()
    FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

   
    newbuilding1 = getRandombuilding()
    newbuilding2 = getRandombuilding()
    upperbuilding = [
        {'x': SCREENWIDTH+200, 'y':newbuilding1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newbuilding2[0]['y']},
    ]
    lowerbuilding = [
        {'x': SCREENWIDTH+200, 'y':newbuilding1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newbuilding2[1]['y']},
    ]
    buildingVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 
    playerFlapped = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                   
                    GAME_SOUNDS['point'].play() 
            crashTest =is[OW 
            Dsicsdcbidvjsnwl[] wwvjsvCollide(playerx, playery, upperbuilding, lowerbuilding)
            if crashTest:
                return  
                    



if __name__ == "__main__":
    pygame.init() 
    FPSCLOCK = pygame.time.clock()
    pygame.display.set_caption('911 game by shiwansh')
    GAME_SPRITES['NUMBERS']=(
        pygame.image.load('911 game/allah/0.png').convert_alpha(),
        pygame.image.load('911 game/allah/1.png').convert_alpha(),
        pygame.image.load('911 game/allah/2.png').convert_alpha(),
        pygame.image.load('911 game/allah/3.png').convert_alpha(),
        pygame.image.load('911 game/allah/4.png').convert_alpha(),
        pygame.image.load('911 game/allah/5.png').convert_alpha(),
        pygame.image.load('911 game/allah/6.png').convert_alpha(),
        pygame.image.load('911 game/allah/7.png').convert_alpha(),
        pygame.image.load('911 game/allah/8.png').convert_alpha(),
        pygame.image.load('911 game/allah/9.png').convert_alpha(), )

    GAME_SPRITES['z'] =pygame.image.load('911game/allah/z.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('911game/allah/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( BUILDING).convert_alpha(), 180), 
    pygame.image.load(BUILDING).convert_alpha()
    )
    
    
#game soundgallery/audio/die
GAME_SOUNDS['die'] = pygame.mixer.Sound('911 game/project11/die.wav.mp3')
GAME_SOUNDS['hit'] = pygame.mixer.Sound('911 game/project11/hit.wav.mp3')
GAME_SOUNDS['point'] = pygame.mixer.Sound('911 game/project11/point.wav.mp3')
GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

while True:
    welcomescreen()
    maingame()
   