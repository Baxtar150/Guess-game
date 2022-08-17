import tkinter
from tkinter import *
import re


root=Tk()
root.title("Email Validation")
root.geometry("350x400")

# Title= Label(root, text="Email validation", font=("Arial", 15))
# Title.grid

def Email_validate(): 
    UserResponse= Label_Password_Entry.get()
    print(UserResponse)
Email_validate()
    # ch=re.compile("^[\w.!#$%&’*+/]+@[\w]+\.\w{2,3}(\.\w{2,3})?$")
    # rw= ch.search(UserResponse)
    
    # if UserResponse==rw:
    #     print("I love you")
    # else:
    #     print("you are mad")


Mainframe= Frame(root)
Mainframe.grid()

# Label_Title= Label(Mainframe, text="", font=("Arial", 12))
# Label_Title.grid(row=0, column=0)
# Label_Title= Label(Mainframe, text="", font=("Arial", 12))
# Label_Title.grid(row=1, column=0)
Label_Email= Label(Mainframe, text="Email", font=("Arial", 12)).grid(row=0, column=0)

Label_Email_Entry= Entry(Mainframe, font=("Arial", 16))
Label_Email_Entry.grid(row=0, column=2)

Label_Password= Label(Mainframe, text="Password", font=("Arial", 12)).grid(row=1, column=0)

Label_Password_Entry= Entry(Mainframe, font=("Arial", 16))
Label_Password_Entry.grid(row=1, column=2)

Validate_Btn= Button(Mainframe, text="Validate", width=10, font=("Arial", 11), bg="#6833FF", command=Email_validate)
Validate_Btn.grid(row=2, column=2)

root.mainloop()