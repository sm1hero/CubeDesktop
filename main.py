import frameMenu as fm
import initalSetup as init
import consts as c
import tkinter as tk
from frameMenu import interfaceMenu as IM


if __name__ == "__main__":

    window =  init.createWindow(
        width  = c.WINDOW_WIDTH,
        height = c.WINDOW_HEIGHT,
        title  = c.WINDOW_TITLE)
    
    if(c.STATE_MENU):
        frame = IM().getButtons(window)
        


    window.mainloop()


