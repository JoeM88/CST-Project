#FileName: Final CST Project.py
#Description: The final project will be another game that will incorporate
#the multimedia aspect by increasing the frequency of the sound in the game
#as the user progresses throught the game.
#Date: 4/13/15
#Version:1
#Compiler: Python 3.4

import pygame, sys, time, random
#To be able to use pygame
#To be able to use the time module
#To be able to use the random functions


from classes import *

pygame.init()
#To be able to use all of pygames features

#This will display the screen of the game with the size of 740 by 830
display_height = 740
display_width = 830

#Screen of the game with the height and width
screen = pygame.display.set_mode((display_width, display_height),0,32)

#The clock of the game to keep track of time
clock = pygame.time.Clock()

bug = Bug(0,100,259,194,"C:\\Users\\Joseph Molina\\Desktop\\CST\\enemy1.png")
bug2 = Bug(0,300,259,194,"C:\\Users\\Joseph Molina\\Desktop\\CST\\enemy1.png")
bug3 = Bug(0,200,259,194,"C:\\Users\\Joseph Molina\\Desktop\\CST\\enemy1.png")



#RGB values for the colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0, 255)
orange = (255,128,128)
gray = (128,128,128)
silver = (192,192,192)

          



#Loading the music for the title screen of the game and playing it infintely.
pygame.mixer.music.load('C:\\Users\Joseph Molina\Desktop\\CST\\KeyGen.ogg')
pygame.mixer.music.play(-1)

#Loading the image of the background
backgroundImg = pygame.image.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\background2.jpg')


#Game loop 
while True:
    #This is so the program can be closed properly by pressing the X
    #This is a list for all the possible pygame.event frameworks
    for event in pygame.event.get():
        #If the type of event is that the program wants to quit then we close pygame and make sure our program closes accordingly
        if event.type == pygame.QUIT:
            pygame.quit()
            #Terminates our program
            sys.exit()
    bug.motion()

    screen.fill((0,0,0))
    
    BaseClass.allsprites.draw(screen)

    

#Bliting the image of the background into the screen at the given coordinates
    #screen.blit(backgroundImg, (0,0))

    #Makes sure that everything is being drawn on the screen
    pygame.display.flip()
    

#How many frames are going to be in a second
clock.tick(24)

