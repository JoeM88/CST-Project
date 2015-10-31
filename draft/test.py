from tkinter import *

class Application(Frame):
    """A GUI application with three buttons."""
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
    #Will create the 3 buttons

        self.button1 = Button(self, text = "Start Game!")
        self.button1.grid()

        #Create second button
        self.button2 = Button(self)
        self.button2.grid() #Grid is like blitting to the screen
        self.button2.configure(text = "Quit Game")

        #Create third button
        self.button3 = Button(self)
        self.button3.grid()
        self.button3.configure(text = "How to play")

root = Tk()
#Setting the title of the game
root.title("CST Final Project")

#Setting the size of the screen
root.geometry("740x830")

app = Application(root)

root.mainloop()
