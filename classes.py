import pygame
pygame.init()
#inherits the sprite class, contains code for collision detection
class BaseClass(pygame.sprite.Sprite):

    #similiar to a python list but contains sprites and deals with sprites
    #Enables us to do collision detection and drawing sprites to screen in one commanad
    #This will be a list containing all sprites in the game
    allsprites = pygame.sprite.Group()
    
    def __init__(self, x, y, width, height, image_string):

        #Calling the  constructor of the class which allows us to access variables image and rect
        pygame.sprite.Sprite.__init__(self) #self because it does not have any parameters just itself


        #A method to add sprites to the class
        BaseClass.allsprites.add(self)

        #The image variable from the sprite class
        self.image = pygame.image.load(image_string)
        
        #Gets dimension of picture to rectangle
        #The absolute rectanle of our image, so we can get dimensions of our rectangle
        self.rect = self.image.get_rect()
        
        #The starting x,y position of the rectangle
        self.rect.x = x #Specifying the x and y coordinates of the rectangle
        self.rect.y = y

        self.width = width #Specifying the width and height from what was given
        self.height = height


class Bug(BaseClass):
    #Another pygame list, for a bug specific group
    List = pygame.sprite.Group()

    #Automatically called when you make an object from the BaseClass
    def __init__(self, x, y, width, height, image_string):
        
        BaseClass.__init__(self, x, y, width, height, image_string)
        
        #Add bug to the list when they are created
        Bug.List.add(self)
        
        self.velx, self.vely = 0,8
        self.jumping, self.go_down = False, False

    def motion(self, SCREENWIDTH, SCREENHEIGHT):
        predicted_location = self.rect.x + self.velx
        if predicted_location < 0:
            self.velx = 0
        
        elif predicted_location + self.width > SCREENWIDTH:
            self.velx = 0
            
        self.rect.x += self.velx
        self.__jump(SCREENHEIGHT)

    def __jump(self,SCREENHEIGHT):
        max_jump = 25
        if self.jumping:
            
            if self.rect.y < max_jump:
                self.go_down = True

            if self.go_down:
                self.rect.y += self.vely

                predicted_location = self.rect.y + self.vely

                if predicted_location + self.height > SCREENHEIGHT:
                    self.jumping = False
                    self.go_down = False
            else:
                self.rect.y -= self.vely
            
        

class Killer(BaseClass):

	List = pygame.sprite.Group()
	def __init__(self, x, y, width, height, image_string):
		BaseClass.__init__(self, x, y, width, height, image_string)
		Killer.List.add(self)

