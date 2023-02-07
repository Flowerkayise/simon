import pygame, sys
from pygame.locals import *
YELLOW= (155,155,0)
BLUE= (0,0,155)
RED= (155,0,0)
GREEN=(0,155,0)

BRIGHTRED = (255,0,0)
RED = (155,0,0)
BRIGHTREDGREEN = (0,255,0)
GREEN = (0,155,0)
BRIGHTBLUE =(0,0,255)
BLUE = (0,0,155)
BRIGHTYELLOW =(255,255,0)
YELLOW =(155,155,0)

REDRECT = pygame.Rect(20,20,200,200)
BLUERECT = pygame.Rect(20,20,200,200)
YELLOWRECT = pygame.Rect(20,20,200,200)
GREENRECT = pygame.Rect(20,20,200,200)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Hello World!')
def getButtonClicked(x,y):
  if YELLOWRECT.collidepoint((x, y)):
    return YELLOW
  elif BLUERECT.collidepoint((x, y)):
    return BLUE
  elif REDRECT.collidepoint((x, y)):
    return RED
  elif GREENRECT. collidepoint((x, y)):
    return GREEN
  return None
def flashButtonAnimation(color):
  if color == YELLOW:
    locationTuple = YELLOWRECT.topleft
    flashcolor = BRIGHTYELLOW
    sound = BEEP1
  elif color == BLUE:
    locationTurple = BLUERECT.topleft
    flashColor = BRIGHTRED
    sound = BEEP2
  elif color == GREEN:
    locationTurple = GREENRECT.toplleft
    flashcolor = BRIGHTGREEN
    sound = BEEP4
  sound.play()
  pygame.draw .rect(DISPLAYSURF,flashColor,(locationTulpe[0],locationTurple[1],200,200))
  pygame.display. update()
  pygame.time.wait(500)
  drawButtons()
  pygame.display.update()


while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == MOUSEBUTTONUP:
      mousex, mousey = event.pos
      clickedButton = getButtonClicked(mousex ,mousey)
      flashButtonAnimation(clickedButton)

  pygame.draw.rect(DISPLAYSURF,YELLOW,(140,145,100,100))
  pygame.draw.rect(DISPLAYSURF,BLUE,(13,25,100,100))
  pygame.draw .rect(DISPLAYSURF,RED,(140,25,100,100))
  pygame.draw.rect(DISPLAYSURF,GREEN,(12,145,100,100))
  pygame.display.update()
