import tkinter
from tkinter import LEFT, Tk
import re

outPut_label.configure(text= str1, justify=LEFT)
root = Tk()
root.title("Email Login")
width= 400
height=300
screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
x = screen_width//2 - width//2
y = screen_height//2 - height//2

root.geometry(f'{width}x{height}+{x}+{y}')


root.mainloop()
# text= "email121&@gmail.com.uk"
# ch=re.compile("^[a-zA-Z0-9.!#$%&’*+/]+@[a-zA-Z0-9]+\.\w{2,3}(\.\w{2,3})?$")
# rw= ch.search(text)
# print(rw)