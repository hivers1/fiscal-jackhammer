import os
import pygame
import pygame.image
import Cgalaga2

pygame.init()

display_width = 640
display_height = 480

gameDisplay = pygame.display.set_mode((display_width,display_height))

gameDisplay.fill((255,255,255))
highscore = 0
h_on = False
num_en = 0
# intro loop
while(True):
    Spaceyimg = pygame.image.load('spacey1.jpg')
    gameDisplay.blit(Spaceyimg,(-350,-25))

    # Title
    largeText = pygame.font.Font('freesansbold.ttf',75)
    textSurface = largeText.render('Spacey in Space', True, (0,255,255))
    rect = textSurface.get_rect()
    rect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurface, rect)

    # go
    pygame.draw.rect(gameDisplay, (0,200,0),(75,350,100,50))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurface = smallText.render('Go', True, (0,0,0))
    rect = textSurface.get_rect()
    rect.center = ( (75+(100/2)), (350+(50/2)) )
    gameDisplay.blit(textSurface, rect)

    # Quit
    pygame.draw.rect(gameDisplay, (200,0,0),(475,350,100,50))
    textSurface = smallText.render('Quit', True, (0,0,0))
    rect = textSurface.get_rect()
    rect.center = ( (475+(100/2)), (350+(50/2)) )
    gameDisplay.blit(textSurface, rect)

    # highscore
    pygame.draw.rect(gameDisplay, (200,0,200),(0,0,100,50))
    disp = 'highscore'
    if h_on:
        disp = str(highscore)
    textSurface = smallText.render(disp, True, (0,0,0))
    rect = textSurface.get_rect()
    rect.center = ( ((100/2)), ((50/2)) )
    gameDisplay.blit(textSurface, rect)
    # Button actions
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if 75+100 > mouse[0] > 75 and 350+50 > mouse[1] > 350:
                num_en += 5
                x = Cgalaga2.run().main(num_en)
                if x > highscore:
                    highscore = x
            if 475+100 > mouse[0] > 475 and 350+50 > mouse[1] > 350:
                pygame.quit()
                quit()
            if 100 > mouse[0] > 0 and 50 > mouse[1] > 0:
                if h_on:
                    h_on = False
                else:
                    h_on = True
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
        pygame.time.Clock().tick(15)
