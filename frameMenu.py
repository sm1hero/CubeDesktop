import tkinter as tk
import consts  as c

class interfaceMenu():
    def getButtons(self, window):
        
        btnRasp  = tk.Button(window, text="Расписание",
              font=(c.TEXT_FONT, c.TEXT_FONT_SIZE),
                width=c.BUTTON_WIDTH, height=c.BUTTON_HEIGHT)
        
        btnVideo  = tk.Button(window, text="Видео о нас",
              font=(c.TEXT_FONT, c.TEXT_FONT_SIZE),
                width=c.BUTTON_WIDTH, height=c.BUTTON_HEIGHT)
        
        btnRasp.grid( column=0, row=0)
        btnVideo.grid(column=1, row=0)

        btnRasp.place(x = ((int(c.WINDOW_WIDTH) / 2)) - 200)
        
        btnVideo.place()
        

        return window

    

