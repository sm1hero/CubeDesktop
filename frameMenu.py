import tkinter as tk
import consts  as c

class interfaceMenu():
    def getButtons(self, window):
        
        btnRasp  = tk.Button(window, text="Расписание",
              font=(c.TEXT_FONT, c.TEXT_FONT_SIZE),
                width=c.BUTTON_WIDTH, height=c.BUTTON_HEIGHT)
        
        btnVideo = tk.Button(window, text="О нас", font=(c.TEXT_FONT, c.TEXT_FONT_SIZE))
        
        btnRasp.grid( column=0, row=0)
        btnVideo.grid(column=1, row=0)

        btnRasp.place(x = ((int(c.WINDOW_WIDTH) / 2) - int(c.BUTTON_WIDTH * 20)),
                      y = ((int(c.WINDOW_HEIGHT) / 2) + int(c.BUTTON_HEIGHT * 100)))
        
        return window

    

