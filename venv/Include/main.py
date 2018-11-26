import pygame, sys
from pygame.locals import *



# global variables and initializations ----------------------------------------------------------------------------------------------------
FPS = 60 # frames per second
WINDOWWIDTH = 1200
WINDOWHEIGHT = 600 # screen resolution for windowed mode
pygame.init()  # initialize
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # resolution
pygame.display.set_caption('Into the Elysium') # windows title
FPSCLOCK = pygame.time.Clock() # initialize the frame counter

mouseClicked = pygame.mouse.get_pressed()  # variable to store mouse clicks
mousePosition = pygame.mouse.get_pos()     # variable to store mouse position

gameMenuFont = pygame.font.Font("fonts\specialelite.ttf", 20)  # font used for menu and settings
titleScreenFont = pygame.font.Font("fonts\changa.ttf", 60)  # font used for the game title
halfOfScreenWidth = WINDOWWIDTH / 2  # half of the screen's width (resolution) to calculate the center independently of the resolution
halfOfScreenHeight = WINDOWHEIGHT / 2  # half of the screen's height (resolution) to calculate the center independently of the resolution
bottomRightWidth = WINDOWWIDTH * 0.8  # relative position of the "click..." box
bottomRightHeight = WINDOWHEIGHT * 0.8  # relative position of the "click..." box




# colours            (R   G    B) -------------------------------------------------------------------------------
TITLESCREENCOLOUR =  (41,  0,  0)
GAMETITLECOLOUR =    (235, 90, 0)
# --------------------------------------------------------------------------------------------------------------


def gameIntro(goToTheMainMenu=None):  # displays title screen
    intro = True # flag to execute intro

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE): # ESC exits
                pygame.quit()
                quit()

        mouseClicked = pygame.mouse.get_pressed()  # variable to store mouse clicks
        mousePosition = pygame.mouse.get_pos()  # variable to store mouse position

        if mouseClicked[0] == 0: # if the mouse hadn't been clicked, the title screen will be displayed
            gameTitle = titleScreenFont.render('Into the Elysium', True, GAMETITLECOLOUR,None)  # creates the title object
            gameTitlePosition = gameTitle.get_rect()  # object to position the title on the screen
            gameTitlePosition.center = (halfOfScreenWidth, halfOfScreenHeight)  # de facto position of the game title
            DISPLAYSURF.fill(TITLESCREENCOLOUR)  # title screen background
            DISPLAYSURF.blit(gameTitle, gameTitlePosition)  # blit the  game title
            pressAnyKey = gameMenuFont.render('Click anywhere to continue', True, GAMETITLECOLOUR,None)  # click to access the main menu and settings
            pressAnyKeyPosition = pressAnyKey.get_rect()  # object to position "click..." box
            pressAnyKeyPosition.center = (bottomRightWidth, bottomRightHeight) # centers the box
            DISPLAYSURF.blit(pressAnyKey, pressAnyKeyPosition)  # draws "click..." text

        if mouseClicked[0] == 1 and goToTheMainMenu != None: # if the button is clicked and the main menu function is passed, it executes the main function
            intro = False
            goToTheMainMenu()

        pygame.display.update() # refreshes the screen
        FPSCLOCK.tick(FPS) # frame counter tick


def gameMainMenu(): # main menu and settings
    menuFlag = True # variable that controls the menu loop

    DISPLAYSURF.fill(TITLESCREENCOLOUR)  # title screen background
    nextScreen = gameMenuFont.render('_next_screen_', True, GAMETITLECOLOUR,None)  # click to access the main menu and settings
    nextScreenPosition = nextScreen.get_rect()  # object to position "click..." box
    nextScreenPosition.center = (halfOfScreenWidth, halfOfScreenHeight)
    DISPLAYSURF.blit(nextScreen, nextScreenPosition)  # draws "click..." text



def main ():
    global FPSCLOCK, DISPLAYSURF # global declaration of frame counter and display surface object

    while True: # main game loop

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE): # x and ESC exits
                pygame.quit()
                sys.exit()

        pygame.display.update() # refreshes the screen
        FPSCLOCK.tick(FPS) # frame counter tick


gameIntro(gameMainMenu)
gameMainMenu()
main()

