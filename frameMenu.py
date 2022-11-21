import tkinter as tk
import consts  as c

class interfaceMenu():
    def getButtons(self, window):
        btnRasp  = tk.Button(window, text="Расписание", font=(c.TEXT_FONT, c.TEXT_FONT_SIZE))
        btnVideo = tk.Button(window, text="О нас", font=(c.TEXT_FONT, c.TEXT_FONT_SIZE))
        btnBack  = tk.Button(window, text="Назад", font=(c.TEXT_FONT, c.TEXT_FONT_SIZE))
    
        btnRasp.grid( sticky=tk.S + tk.N)
        btnVideo.grid(column=1, row=0, sticky=tk.S + tk.N)
        btnBack.grid(column=2, row=0, sticky=tk.S + tk.N)
        return window

    

