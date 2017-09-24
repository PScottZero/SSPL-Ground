# STP Ground Station GUI
# Student Space Programs Laboratory
#
# 24 September 2017
from tkinter import *


# builds GUI elements
class STPGround:

    # initializer class
    def __init__(self, master):
        self.logo = PhotoImage(file="logo.png")
        self.logoLabel = Label(master, image=self.logo, borderwidth=0, highlightthickness=0, bg="grey")
        self.logoLabel.image = self.logo
        self.logoLabel.pack()


# configures the root window of the application
root = Tk()
root.configure(bg="grey")
root.title("SSPL STP Ground Station")
root.geometry("500x500")
root.resizable(width=False, height=False)

# image icon for application
img = PhotoImage(file="icon.png")
root.call("wm", "iconphoto", root, img)

# assembles and runs GUI
STPGround(root)
root.mainloop()
