import tkinter
from tkinter import Tk, messagebox

#initailizing our window and other form module

root = Tk()
root.title('Login Form -  Glimpse Solution')
width= 400
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width//2 - width//2
y = screen_height//2 - height//2

root.geometry(f'{width}x{height}+{x}+{y}')


root.mainloop()