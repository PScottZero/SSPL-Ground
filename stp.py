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
        self.middleFrame.pack(anchor="w", padx=20, pady=(30, 0))
        self.lowerFrame = Frame(master, bg="grey")
        self.lowerFrame.pack(anchor="w", padx=20)

        # initializes logo for upper frame
        self.logo = PhotoImage(file="logo.png")
        self.logoLabel = Label(self.upperFrame, image=self.logo, borderwidth=0, highlightthickness=0, bg="grey")
        self.logoLabel.image = self.logo
        self.logoLabel.pack()

        # latitude cell
        self.latitude = StringVar()
        self.widget_creator(self.latitude, "Latitude:", 0, 0, 0)

        # longitude cell
        self.longitude = StringVar()
        self.widget_creator(self.longitude, "Longitude:", 20, 0, 1)

        # gas 1 concentration cell
        self.gas1 = StringVar()
        self.widget_creator(self.gas1, "Gas 1 Concentration", 0, 1, 0)

        # gas 2 concentration cell
        self.gas2 = StringVar()
        self.widget_creator(self.gas2, "Gas 2 Concentration", 20, 1, 1)

        # temperature cell
        self.temperature = StringVar()
        self.widget_creator(self.temperature, "Temperature:", 0, 2, 0)

        # altitude cell
        self.altitude = StringVar()
        self.widget_creator(self.altitude, "Altitude:", 20, 2, 1)

        # altitude graph (dummy data)
        self.graph = Canvas(self.lowerFrame, width=660, height=230, bg="white", borderwidth=0, highlightthickness=0)

        # vertical axis (height meters)
        self.graph.create_line(30, 0, 30, 200)
        self.graph.create_line(30, 200, 660, 200)
        self.graph.create_line(0, 230, 30, 200)
        self.graph.create_line(30, 150, 35, 150)
        self.graph.create_line(30, 100, 35, 100)
        self.graph.create_line(30, 50, 35, 50)
        self.graph.create_text(15, 20, text="m")
        self.graph.create_text(15, 50, text="150")
        self.graph.create_text(15, 100, text="100")
        self.graph.create_text(15, 150, text="50")
        self.graph.create_text(15, 200, text="0")

        # horizontal axis (time seconds)
        self.graph.create_line(100, 200, 100, 195)
        self.graph.create_line(170, 200, 170, 195)
        self.graph.create_line(240, 200, 240, 195)
        self.graph.create_line(310, 200, 310, 195)
        self.graph.create_line(380, 200, 380, 195)
        self.graph.create_line(450, 200, 450, 195)
        self.graph.create_line(520, 200, 520, 195)
        self.graph.create_line(590, 200, 590, 195)
        self.graph.create_text(30, 215, text="0")
        self.graph.create_text(100, 215, text="15")
        self.graph.create_text(170, 215, text="30")
        self.graph.create_text(240, 215, text="45")
        self.graph.create_text(310, 215, text="60")
        self.graph.create_text(380, 215, text="75")
        self.graph.create_text(450, 215, text="90")
        self.graph.create_text(520, 215, text="100")
        self.graph.create_text(590, 215, text="120")
        self.graph.create_text(630, 215, text="sec")

        self.graph.pack()

        # sets dummy data
        self.dummy_data()

    # creates data cells
    def widget_creator(self, variable, text, padding, row, col):
        widget_frame = Frame(self.middleFrame, bg="#c1c1c1", width=320, height=100)
        widget_frame.grid_propagate(0)
        widget_frame.grid_columnconfigure(0, weight=1)
        widget_frame.grid(padx=(padding, 0), pady=(0, 20), row=row, column=col)
        widget_label = Label(widget_frame, bg="#c1c1c1", text=text, fg="blue", font=("Arial", 16))
        widget_label.config(pady=10)
        widget_label.grid()
        widget_value = Label(widget_frame, bg="#c1c1c1", textvariable=variable, font=("Arial", 20))
        widget_value.grid()

    # dummy data for GUI
    def dummy_data(self):
        self.latitude.set("38 54 N")
        self.longitude.set("77 02 W")
        self.gas1.set("77%")
        self.gas2.set("42%")
        self.temperature.set("22C")
        self.altitude.set("439ft")
        self.graph.create_line(30, 200, 310, -50, 450, 100, fill="red", smooth=True)
        self.graph.create_oval(445, 95, 455, 105, fill="red")


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
