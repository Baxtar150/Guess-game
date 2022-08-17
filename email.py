
import re

text= input("")
def confirm():
    
    ch=re.compile("^[a-zA-Z0-9.!#$%&’*+/]+@[a-zA-Z0-9]+\.\w{2,3}(\.\w{2,3})?$")
    rw= ch.search(text)
    print(rw)
confirm()

# text= "email121&@gmail.com"
# ch= re.compile("^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$")
# rw= ch.search(text)

# print(rw)

