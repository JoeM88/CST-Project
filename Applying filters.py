from PIL import Image
from PIL import ImageFilter

#Opening up an image and applying a filter to it, then saving it
img = Image.open("C:\\Users\\Joseph Molina\\Desktop\\CST\\space.jpg")
imgout = img.filter(ImageFilter.FIND_EDGES)
img.show()
imgout.show()
imgout.save("anything3.jpg")
