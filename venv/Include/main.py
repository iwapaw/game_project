import pygame, sys
from pygame.locals import *


# global variables
FPS = 60 # frames per second
WINDOWWIDTH = 1200
WINDOWHEIGHT = 600 # screen resolution for windowed mode


# colours            (R   G    B)
TITLESCREENCOLOUR =  (41,  0,  0)
GAMETITLECOLOUR =    (235, 90, 0)


def main ():
    global FPSCLOCK, DISPLAYSURF # global declaration of frame counter and display surface object
    pygame.init() # initialize
    FPSCLOCK = pygame.time.Clock() # initialize the frame counter
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # resolution
    pygame.display.set_caption('_the_game_') # windows title

    mouseClicked = False  # variable to store mouse clicks
    mousex = 0 # stores the posistion of the cursor event (horizontal)
    mousey  = 0 # stores the posistion of the cursor event (horizontal)
    gameMenuFont = pygame.font.Font("fonts\specialelite.ttf", 20)  # font used for menu and settings
    titleScreenFont = pygame.font.Font("fonts\changa.ttf", 60)  # font used for the game title
    halfOfScreenWidth = WINDOWWIDTH / 2  # half of the screen's width (resolution) to calculate the center independently of the resolution
    halfOfScreenHeight = WINDOWHEIGHT / 2  # half of the screen's height (resolution) to calculate the center independently of the resolution
    bottomRightWidth = WINDOWWIDTH * 0.8  # relative position of the "click..." box
    bottomRightHeight = WINDOWHEIGHT * 0.8  # relative position of the "click..." box




    while True: # main game loop

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE): # x and ESC exits
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION: # tracks the mouse motion
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP: # tracks whether the mouse button was clicked
                mousex, mousey = event.pos
                mouseClicked = True

                # ------------------------------------------------- MAIN MENU ----------------------------------------------------------------------------------
                if not mouseClicked:
                    gameTitle = titleScreenFont.render('_game_title_', True, GAMETITLECOLOUR,None)  # creates the title object
                    gameTitlePosition = gameTitle.get_rect()  # object to position the title on the screen
                    gameTitlePosition.center = (halfOfScreenWidth, halfOfScreenHeight)  # de facto position of the game title
                    DISPLAYSURF.fill(TITLESCREENCOLOUR)  # title screen background
                    DISPLAYSURF.blit(gameTitle, gameTitlePosition)  # blit the  game title
                    pressAnyKey = gameMenuFont.render('Click anywhere to continue', True, GAMETITLECOLOUR,None)  # click to access the main menu and settings
                    pressAnyKeyPosition = pressAnyKey.get_rect()  # object to position "click..." box
                    pressAnyKeyPosition.center = (bottomRightWidth, bottomRightHeight)
                    DISPLAYSURF.blit(pressAnyKey, pressAnyKeyPosition)  # draws "click..." text
                if mouseClicked:
                    nextScreen = gameMenuFont.render('_next_screen_', True, GAMETITLECOLOUR,None)  # click to access the main menu and settings
                    nextScreenPosition = nextScreen.get_rect()  # object to position "click..." box
                    nextScreenPosition.center = (halfOfScreenWidth, halfOfScreenHeight)
                    DISPLAYSURF.blit(nextScreen, nextScreenPosition)  # draws "click..." text


        pygame.display.update() # refreshes the screen
        FPSCLOCK.tick(FPS) # frame counter tick




###

main()

