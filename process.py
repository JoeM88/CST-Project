#Importing the necessary modules 
import pygame, sys, random, classes


def process(bug, FPS, total_frames, SCREENHEIGHT, score):
    #Processing

    for event in pygame.event.get():
        #If the type of event is that the program wants to quit then we close pygame and make sure our program closes accordingly
        if event.type == pygame.QUIT:
            pygame.quit()
            #Terminates our program
            sys.exit()
    #Declaring a variable that will be used to determine what key was pressed     
    keys = pygame.key.get_pressed()
    
    #if statements with statements to excute when the right key is pressed.
    if keys[pygame.K_RIGHT]:
        #once the right key is pressed the main character will move to the right.
        classes.Bug.going_right = True
        #The image of the main character facing in the right direction will loaded.
        bug.image = pygame.image.load("C:\\Users\\Joseph Molina\\Desktop\\CST\\flippedEnemy1.png")
        #The position of the main character will change.
        bug.velx = 5
        #If statements with lines of code to be excuted once the left key is pressed
        
    elif keys[pygame.K_LEFT]:
        #The character will now be facing in the left direction.
        classes.Bug.going_right = False
        #The image of the character moving in the left direction will be loaded.
        bug.image = pygame.image.load("C:\\Users\\Joseph Molina\\Desktop\\CST\\enemy1.png")
        #The position of the character will be moved.
        bug.velx = -5
        
    else:
        #if none of the keys above are pressed nothing will occur to the main character
        bug.velx = 0
        
    #If statement with lines of code to be executed once it is pressed
    if keys[pygame.K_UP]:
        #once the up key is pressed the sound effect will be loaded then played once.
        pygame.mixer.music.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\jump.ogg')
        pygame.mixer.music.play(1)
        #Boolean value of the character jumping will be set to True.
        bug.jumping = True
        
    #IF statements with lines of code to be executed once the space key is pressed.    
    if keys[pygame.K_SPACE]:
        pygame.mixer.music.load('C:\\Users\\Joseph Molina\\Desktop\\CST\\lasersound.ogg')
        pygame.mixer.music.play(1)
        p = classes.BugProjectile(bug.rect.x, bug.rect.y, 34, 34, "projectile.gif")
        if classes.Bug.going_right:
            p.velx = 8
        else:
            p.image = pygame.transform.flip(p.image, True, False)
            p.velx = -8

    #Calling out the spawn and collision functions with the given parameters
    spawn(FPS, total_frames, SCREENHEIGHT,score)
    collisions()
#Function that will handle the spawning of the enemies
def spawn(FPS, total_frames, SCREENHEIGHT, score):
    #Setting up variables that will help determine the time intervals
    #from which the enemies should be spawned at
    four_seconds = FPS * 4
    one_second = FPS * 1

    
    if score > 300:
        if total_frames % one_second == 0:
            r = random.randint(1, 2)
            x = 1
            if r == 2:
                x = 1400 - 120
            enemy = classes.Enemy(x, SCREENHEIGHT - 110, 120, 120, "C:\\Users\\Joseph Molina\\Desktop\\CST\\ghost.png")
    else:
        if total_frames % four_seconds == 0:
            #random spawn sights
            r = random.randint(1, 2)
            x = 1
            if r == 2:
                x = 1400 - 120
            enemy = classes.Enemy(x, SCREENHEIGHT - 110, 120, 120, 'C:\\Users\\Joseph Molina\\Desktop\\CST\\ghost.png')
            
#Function will handle the collision of the projectile and the enemy      
def collisions():
    for enemy in classes.Enemy.List:
        proj = pygame.sprite.spritecollide(enemy, classes.BugProjectile.List, True)
        if len(proj) > 0:
            for hit in proj:
                enemy.health -= enemy.half_health





