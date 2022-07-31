# -*- coding: utf-8 -*-
from tkinter import Tk, Button
from scripts import record_volume
from tkinter import messagebox
from sys import exit

class main:
    def __init__(self):
        self.window = Tk()
        self.window.title('ip calculate')
        
        self.window.minsize(width=300, height=200)
        self.button = Button(self.window,
                             text="Старт",
                             width=20,
                             height=2,
                             bg="white",
                             fg="black",
                             command=record_volume)
        self.button.pack()
        self.button = Button(self.window,
                             text="Стоп",
                             width=20,
                             height=2,
                             bg="white",
                             fg="black")
        self.button.pack()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.window.destroy()
            exit()
