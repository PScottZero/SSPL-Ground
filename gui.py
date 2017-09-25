# STP Ground Station GUI
# Student Space Programs Laboratory
#
# 24 September 2017
from tkinter import *


# builds GUI elements
class STPGround:

    # initializer class
    def __init__(self, master):

        # initializes upper and lower frames
        self.upperFrame = Frame(master, bg="grey")
        self.upperFrame.pack()
        self.middleFrame = Frame(master, bg="grey")
        self.middleFrame.pack(anchor="w", padx=20, pady=40)
        self.lowerFrame = Frame(master, bg="grey")
        self.lowerFrame.pack(anchor="w", padx=20)

        # initializes logo for upper frame
        self.logo = PhotoImage(file="logo.png")
        self.logoLabel = Label(self.upperFrame, image=self.logo, borderwidth=0, highlightthickness=0, bg="grey")
        self.logoLabel.image = self.logo
        self.logoLabel.pack()

        # temperature widget
        self.temperature = StringVar()
        self.widget_creator(self.temperature, "Temperature:", 0)

        # GPS latitude widget
        self.latitude = StringVar()
        self.widget_creator(self.latitude, "Latitude:", 1)

        # GPS longitude widget
        self.longitude = StringVar()
        self.widget_creator(self.longitude, "Longitude:", 2)

        # gas 1 widget
        self.gas1 = StringVar()
        self.widget_creator(self.gas1, "Gas 1 Concentration:", 3)

        # gas 2 widget
        self.gas2 = StringVar()
        self.widget_creator(self.gas2, "Gas 2 Concentration:", 4)

        # altitude widget
        self.altitude = StringVar()
        self.widget_creator(self.altitude, "Altitude:", 5)

        # altitude graph (dummy data)
        self.graph = Canvas(self.lowerFrame, width=660, height=250, bg="white", borderwidth=0, highlightthickness=0)
        self.graph.create_line(0, 250, 100, 50, fill="red")
        self.graph.create_line(100, 50, 200, 150, fill="red")
        self.graph.create_line(200, 150, 300, 50, fill="red")
        self.graph.create_line(300, 50, 400, 200, fill="red")
        self.graph.create_line(400, 200, 500, 100, fill="red")
        self.graph.create_line(500, 100, 660, 50, fill="red")
        self.graph.pack()

        # sets dummy data for all fields
        self.dummy_data()

    # creates widgets for data
    def widget_creator(self, widget_var, name, n):
        widget_label = Label(self.middleFrame, text=name, fg="blue", bg="grey", font=("Arial", 16))
        widget_label.config(padx=10, pady=10)
        widget_label.grid(row=n, column=0, sticky=W)
        widget_var.set("NULL")
        widget_data = Label(self.middleFrame, textvariable=widget_var, bg="grey", font=("Arial", 16))
        widget_data.config(padx=10, pady=10)
        widget_data.grid(row=n, column=2, sticky=W)

    # sets dummy data for all fields
    def dummy_data(self):
        self.temperature.set("22C")
        self.latitude.set("38 54 N")
        self.longitude.set("77 02 W")
        self.gas1.set("77%")
        self.gas2.set("42%")
        self.altitude.set("439ft")


# configures the root window of the application
root = Tk()
root.title("SSPL STP Ground Station")
root.configure(bg="grey")
root.geometry("700x700")
root.resizable(width=False, height=False)

# image icon for application
img = PhotoImage(file="icon.png")
root.call("wm", "iconphoto", root, img)

# assembles and runs GUI
s = STPGround(root)
root.mainloop()
