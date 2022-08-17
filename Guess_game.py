from ast import Global, Num
from tkinter import *
from random import randint
from tkinter import messagebox
import string 
import random
from string import *

#To create screen(window)
root= Tk() #Tk() is a built in function that produces a creen
root.title("Guess The Number") # root.title creates a title for the screen 
root.geometry("300x400")

#Genarate Number Function
def GenerateNumberFunc():
    global temp2 
    temp = string.digits
    temp_2=random.sample(temp, 4)
    temp2= (temp_2)
    print(''.join(temp2))
    # print(type(temp2))
           


def GuessNumberFunc(): 
    global temp2
    UserResponse= AnswerEntry.get()
    UserResponse2=list(UserResponse)
    print(UserResponse2)
    # print(temp2)
    Resultlabel.config(text=temp2)
    messagebox.showinfo(temp2)
    if UserResponse2==temp2:
        Resultlabel.config(text="Correct", fg="Red")
    else:
        Resultlabel.config(text="Incorrect")

    
#To place a content on the screen 
Title= Label(root, text="Guess The Numbers", font=("Arial", 15))#Label widget is used to had text to the created screen
Title.pack() #.pack() centralizes the content on the screen

#Main Frame
Mainframe=Frame(root) #Frame creates a frame structure for items to be contained.
Mainframe.pack(pady=60)

#Guess the number
GuessNumberlabel= Label(Mainframe, text="Guess Four Numbers From  0 To 9", font=('Arial', 10))
GuessNumberlabel.pack(pady=10)

#Entry widget
AnswerEntry= Entry(Mainframe, font=("Arial", 16)) #Entry widget creates an entry box you can input data.
AnswerEntry.pack(pady=10)

#Button
GenerateBtn= Button(Mainframe, text="Generate Numbers", width=15, font=("Arial", 11), bg="grey",  command=GenerateNumberFunc)
GenerateBtn.pack()

Guessbtn= Button(Mainframe, text="Guess", width=12, font=("Arial", 9), bg="orange", command=GuessNumberFunc)
Guessbtn.pack(pady=10)

Resultlabel= Label(Mainframe, text="", font=("Arial",10))
Resultlabel.pack()

root.mainloop()