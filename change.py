from PIL import Image
from PIL import ImageFilter

#Opening up the space image.
img = Image.open("C:\\Users\\Joseph Molina\\Desktop\\CST\\space.jpg")
#looping through the pixels of the image and applying certain values to the
#RGB values.
for x in range(img.size[0]):
    for y in range(img.size[1]):
        r,g,b = img.getpixel((x,y))
        img.putpixel((x,y),(100,120,50))
#Displaying the image.
img.show()
#Saving the image.
img.save("anything.jpg")
   
