from time import strftime
from tkinter import *
import tkinter
import json

def clock():
    time =strftime('%I:%M:%S %p')
    lblClock.config(text=time, relief='ridge', bd=8)
    lblClock.after(1000,clock)
    lblClock.pack(pady=20)

root = Tk()
root.geometry('400x100')
root.title('Digital Clock')
root.resizable(False, False)
#label into Root
lblClock = Label(root, fg='black', font=('arial', 26, 'bold'))
clock()
root.mainloop()
obj = {'name': 'Adebayo', 'age': 35, 'marital': 'single'}
js = json.dumps(obj,indent=4)
print(js)
