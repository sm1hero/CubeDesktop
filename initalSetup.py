import tkinter as tk
import consts  as c


class createWindow(tk.Tk):
    def __init__(self, width, height, title):
        super().__init__()
        self.geometry(width +"x" + height)
        self.title(title)
        self.setBackground(width, height)        

    def setBackground(self, width, height):
        backgroundImage      = tk.PhotoImage(file = c.WINDOW_BACKGROUND_IMAGE_PATH)
        backgroundImageLogo  = tk.PhotoImage(file = c.WINDOW_BACKGROUND_LOGO)

        background     = tk.Label(image = backgroundImage)
        backgroundLogo = tk.Label(image = backgroundImageLogo, width=100, height=100)

        background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        backgroundLogo.place(x = 10, y = 10)

        background.image = backgroundImage
        backgroundLogo.image = backgroundImageLogo





        
    
        