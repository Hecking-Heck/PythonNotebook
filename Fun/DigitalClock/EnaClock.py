# Imports
from tkinter import *
from time import strftime

# Setting up Tkinter
myWindow = Tk()
myWindow.title('') # I want an empty title bar
myWindow.resizable(False, False) # I do not want the window to be resizeable
myWindow.geometry("350x75") # This is the size I want the window to be
myWindow.iconbitmap("ena.ico") # This is the icon I want to use for the window

# Add image file 
bg = PhotoImage(file = "internetcore_background.png")

# Clock label setup
clock = Label(myWindow, font= ('arial', 40, 'bold'), image= bg, foreground= 'white', compound='center')
clock.pack(anchor= 'center')

# Time Function
def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

# Running time
time()

# Running the main loop
mainloop()