## Stuart McIntosh
## Year 12 Software Design and Development Software Major Project
## Due Date: 09/05/2014

import pygame, random
pygame.init()

#Variable that runs the main Game Loop
Game = True

#Screen
Height = 500
Width = 500
ScreenSize = (Height, Width)
#Colours used in the program, in (R, G, B) format
black = (0, 0, 0)
white = (255, 255, 255)

#Controls the on screen image display and movement
  #Car
car = pygame.sprite.Sprite()
car.image = pygame.image.load('car.png')
car.rect = car.image.get_rect()
car_group = pygame.sprite.GroupSingle(car)
    #Tile setup
TILE_SIZE = car.rect.width
numTileWide = Width / TILE_SIZE
numTileHigh = Height / TILE_SIZE

screenX = numTileWide * TILE_SIZE
screenY = numTileHigh * TILE_SIZE
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("Stuart McIntosh-Yr 12 SDD Major Project")

##-Random Number Generation
ranNum = str(random.randint(0, 9))

##Manages the text to display on screen, including colour and font
textToDisplay = ranNum
font = pygame.font.Font(None, 40)
onScreenText = font.render(textToDisplay, True, black)
onScreenText_display = onScreenText.get_rect(centerx=screenX/2, centery=screenY/2)

###Movement
##s = 'stop'
##u = 'up'
##r = 'right'
##d = 'down'
##l = 'left'
##movedir = s

###Questions Text File
##qtf = open('questions.txt')



#-Game Loop
while Game == True:
    for event in pygame.event.get():
    #Quit Game
      #Close Button
        if event.type == pygame.QUIT:
            Game = False
        if event.type == pygame.KEYDOWN:
          #Escape Key
            if event.key == pygame.K_ESCAPE:
                Game = False
##    if movedir == u:
##        if car.rect.top > 0:
##            car.rect.top -= 1
##    if movedir == r:
##        if car.rect.right < screenY:
##            car.rect.right += 1
##    if movedir == d:
##        if car.rect.bottom < screenX:
##            car.rect.bottom += 1
##    if movedir == l:
##        if car.rect.left > 0:
##            car.rect.left -= 1
    screen.fill(white)
    car_group.draw(screen)
##    screen.blit(TextOne, DisplayOne_View)
    pygame.display.update()
pygame.quit()
