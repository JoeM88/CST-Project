#FileName: Final CST Project.py
#Description: The final project will be another game that will incorporate
#the multimedia aspect by increasing the frequency of the sound in the game
#as the user progresses throught the game.
#Date: 4/13/15
#Version:1
#Compiler: Python 3.4

import pygame, sys
from pygame.locals import *
pygame.font.init()
PYGBUTTON_FONT = pygame.font.Font('freesansbold.ttf', 14)
#To be able to use pygame

import time
#To be able to use the time module

import random
#to be able to use the random function

pygame.init()
#To be able to use all of pygames features

#This will display the screen of the game with the size of 640 by 360
display_height = 360
display_width = 640

#RGB values for the colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0, 255)
orange = (255,128,128)
gray = (128,128,128)
silver = (192,192,192)
DARKGRAY =(64,64,64)
LightGray(212,208,200)






#Screen of the game with the height and width
screen = pygame.display.set_mode((display_width, display_height),0,32)

#The clock of the game to keep track of time
clock = pygame.time.Clock()

#Frames per second
FPS = 24


while True:
    #This is so the program can be closed properly by pressing the X
    #This is a list for all the possible pygame.event frameworks
    for event in pygame.event.get():
        #If the type of event is that the program wants to quit then we close pygame and make sure our program closes accordingly
        if event.type == pygame.QUIT:
            pygame.quit()
            #Terminates our program
            sys.exit()

    i += 3
    if i > 255:
        i%= 255
    screen.fill((45,i,200))
    pygame.draw.line(screen, blue,(0,0),(display_width, display_height), 5)
    pygame.draw.rect(screen, orange,(10,30,300,45))
    pygame.draw.circle(screen,silver,(350,200),80, )

    #Makes sure that everything is being drawn on the screen
    pygame.display.flip()

#How many frames are going to be in a second
clock.tick(FPS)
    
    
    
