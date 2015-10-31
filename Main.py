#FileName: Final CST Project.py
#Description: The final project will be another game that will incorporate
#the multimedia aspect by increasing the frequency of the sound in the game
#as the user progresses throught the game.
#Authors: Joseph Molina and Jose Cortez
#Date: 4/13/15
#Version:1
#Compiler: Python 3.4

import pygame, sys, time, random
from pygame.locals import *
#To be able to use pygame
#To be able to use the time module
#To be able to use the random functions

#Importing the classes and process into the main so it could utilize them
from classes import *
from process import process 

#importing both the image and imagefilter modules to manipulate images
from PIL import Image
from PIL import ImageFilter
from sound import GameMusic

pygame.init()
#To be able to use all of pygames features

#This will display the screen of the game with the size of 740 by 830
SCREENWIDTH = 1400
SCREENHEIGHT = 650

#Screen of the game with the height and width
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT),0,32)

#The clock of the game to keep track of time
clock = pygame.time.Clock()
#Setting the frames per second 
FPS = 24
#total_frames will be used in the enemys movement
total_frames = 0

#Line of code will set the name of the screen
pygame.display.set_caption('Final CST Project')

#RGB values for the colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0, 255)
orange = (255,128,128)
gray = (128,128,128)
silver = (192,192,192)

#Declaring the font and font size for the score
smallfont = pygame.font.SysFont("comicsansms",25)
#setting the window to display the score
gameDisplay = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

#Loading the image of the bug into the bottom left hand corner of the screen
bug = Bug(700,SCREENHEIGHT - 120,200,150,'C:\\Users\\Joseph Molina\\Desktop\\CST\\flippedEnemy1.png')

#Loading the image of an enemy into the right hand corner of the screen
enemy = Enemy(1100,SCREENHEIGHT - 120,120,120,'C:\\Users\\Joseph Molina\\Desktop\\CST\\killer.png')
#Loading a ghost into the right hand corner of the screen 
enemy1 = Enemy(1000,SCREENHEIGHT - 110, 120,120,'C:\\Users\\Joseph Molina\\Desktop\\CST\\ghost.png')
enemy2 = Enemy(1000,SCREENHEIGHT - 110, 120,120,'C:\\Users\\Joseph Molina\\Desktop\\CST\\ghost.png')
enemy3 = Enemy(1000,SCREENHEIGHT - 110, 120,120,'C:\\Users\\Joseph Molina\\Desktop\\CST\\ghost.png')

#Setting up the default font of the letters
font = pygame.font.SysFont(None, 25)

#Function that will display the score
def score(score):
    text = smallfont.render("Score: " + str(score), True, white)
    #Displaying the score in the upper left hand corner of the screen
    gameDisplay.blit(text, [0,0])
    
#Function to display the title of the screen in the game intro
#This function will also display a copyright image before the game initiates
def display_text_animation(string):
    #Loading in the copyright image and also displaying it in the center of the screen
    copyright1 = pygame.image.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\copyright.png')
    screen.blit(copyright1, (SCREENWIDTH/3, 650 / 4.5))
    pygame.display.flip()
    
    #Loading in the typewriter sound effect for the game intro
    pygame.mixer.music.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\typewriter.ogg')
    pygame.mixer.music.play(1)
    
    #For how long the screen to wait
    time.sleep(2)
    #The text is equal to what is inserted into the parameters
    text = ''

    
     #This loop will blit one character of a time from the string array into
     #the screen
    for i in range(len(string)):
        screen.fill(silver)
        text += string[i]
        text_surface = font.render(text, True, black)
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(300)
    pygame.mixer.music.stop()
    
#Game main loop
def main():
    #Loading the music for the title screen of the game and playing it infintely.
    sound = pygame.mixer.Sound('C:\\Users\\Joseph Molina\\Desktop\\CST\\KeyGen.wav')
    sound.play(loops = -1)
    #Boolean to determine which sound file to play
    start_music = True
    #Setting the default value of score
    total_score = 0
    #using time variable as a way to keep track of the seconds
    time = 0
    #Loading the image of the background
    backgroundImg = pygame.image.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\space.jpg')
    while True:
        
        time = time + 1
        #If statement to change the background image of the program
        if time == 300:
            backgroundImg = pygame.image.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\anything.jpg')
        if time == 500:
            backgroundImg = pygame.image.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\space.jpg')
        if time == 700:
            backgroundImg = pygame.image.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\anything3.jpg')
        if time == 900:
            backgroundImg = pygame.image.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\magicEarth.jpg')
        if time == 990:
            backgroundImg = pygame.image.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\space.jpg')
             
        global total_frames
        current_score = BaseClass.total_score
        process(bug, FPS, total_frames, SCREENHEIGHT, current_score)

        #LOGIC
        bug.motion(SCREENWIDTH, SCREENHEIGHT)
        Enemy.update_all(SCREENWIDTH)
        #Enemy.movement(SCREENWIDTH)
        BugProjectile.movement()
        total_frames += 1


        #Bliting the image of the background into the screen at the given coordinates
        screen.blit(backgroundImg, (0,0))
        
        #Draws all the sprites to the screen
        BaseClass.allsprites.draw(screen)
        #If statement to change the pace of the music
        score(BaseClass.total_score)
        if BaseClass.total_score > 300 and start_music:
            start_music = False
            sound.stop()
            GameMusic()
        
        #Makes sure that everything is being drawn on the screen
        pygame.display.flip()
        #How many frames are going to be in a second
        clock.tick(FPS)
        
       
#Calling out the functions in the order of 
display_text_animation('Welcome to Jose and Joseph CST Project!')
main()
pygame.display.update()
time.sleep(2)
