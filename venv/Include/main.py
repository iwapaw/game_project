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

topMenuButtonHeight = WINDOWHEIGHT * 0.3 # for the first button in the main menu
secondMenuButtonHeight = WINDOWHEIGHT * 0.4 # for the second button in the main menu
thirdMenuButtonHeight = WINDOWHEIGHT * 0.5 # for the third button in the main menu
fourthMenuButtonHeight = WINDOWHEIGHT * 0.6 # for the fourth button in the main menu
fullScreenButtonHeight = WINDOWHEIGHT * 0.9 # the location of the fullscreen button in the main menu
fullScreenButtonWidth = WINDOWWIDTH * 0.9 # the location of the fullscreen button in the main menu
halfOfScreenWidth = WINDOWWIDTH / 2  # half of the screen's width (resolution) to calculate the center independently of the resolution
halfOfScreenHeight = WINDOWHEIGHT / 2  # half of the screen's height (resolution) to calculate the center independently of the resolution
bottomRightWidth = WINDOWWIDTH * 0.8  # relative position of the "click..." box
bottomRightHeight = WINDOWHEIGHT * 0.8  # relative position of the "click..." box


gameButtonHeight = WINDOWHEIGHT / 20 # height of the button in the main menu
gameButtonWidth = WINDOWWIDTH / 5    # width of the button in the main menu


# colours                           (R   G    B) -------------------------------------------------------------------------------
TITLESCREENCOLOUR =                 ( 41,  0,  0)
GAMETITLECOLOUR =                   (235, 90,  0)
BLACK =                             (  0,  0,  0)
GAMETITLECOLOURBRIGHTER =           (235,157,  0)
# --------------------------------------------------------------------------------------------------------------


def gameIntro(goToTheMainMenu=None):  # displays title screen
    intro = True # flag to execute intro

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE): # ESC exits
                pygame.quit()
                sys.exit()

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
    mainMenu = True # variable that controls the menu loop

    while mainMenu: # main menu loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        DISPLAYSURF.fill(TITLESCREENCOLOUR)

        onScreenButton('New',halfOfScreenWidth, topMenuButtonHeight, gameButtonWidth, gameButtonHeight, GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER, gameMainMenu, None) # calls the button function - newa game
        onScreenButton('Load', halfOfScreenWidth, secondMenuButtonHeight, gameButtonWidth, gameButtonHeight, GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER, gameMainMenu, None)  # calls the button function - load game
        onScreenButton('Save', halfOfScreenWidth, thirdMenuButtonHeight, gameButtonWidth, gameButtonHeight, GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER, gameMainMenu, None)  # calls the button function - save game
        onScreenButton('Quit', halfOfScreenWidth, fourthMenuButtonHeight, gameButtonWidth, gameButtonHeight, GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER, gameMainMenu, None)  # calls the button function - quit
        onScreenButton('[FS]', bottomRightWidth, bottomRightHeight, gameButtonWidth/4, gameButtonHeight*1.4, GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER, gameMainMenu, None)  # calls the button function - go to full screen

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def onScreenButton(textOnButton, xButtonCoordinate, yButtonCoordinate, buttonWidth, buttonHeight, initialColour, secondColour, fontUsedForButton, actionInvokedByButton=None):
    if xButtonCoordinate + buttonWidth > mousePosition[0] > xButtonCoordinate and yButtonCoordinate + buttonHeight > mousePosition[1] > yButtonCoordinate: # if the cursor is within the box
        pygame.draw.rect(DISPLAYSURF, secondColour, (xButtonCoordinate,yButtonCoordinate,buttonWidth,buttonHeight))                                        # highlights the button with a brighter colour

        if mouseClicked[0] == 1 and actionInvokedByButton != None:    # if the button is clicked
                actionInvokedByButton()                               # go to the function passed to onScreenButton

    else:                                                                                                                   # if the cursor is outside the button
        pygame.draw.rect(DISPLAYSURF, initialColour, (xButtonCoordinate,yButtonCoordinate,buttonWidth, buttonHeight))       # blits a darker colour

    buttonText = gameMenuFont.render(textOnButton, True, BLACK, None) # creates a text object
    buttonPosition = buttonText.get_rect()                            # creates a rect
    buttonPosition.center = (((xButtonCoordinate)+(buttonWidth*2)), ((yButtonCoordinate)+(buttonHeight/2)))  # centers the rect
    #buttonPosition.center = (xButtonCoordinate, yButtonCoordinate)
    DISPLAYSURF.blit(buttonText, buttonPosition)   # blits the object


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

