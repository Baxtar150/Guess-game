import random
import string
# rmd= random.randint(1,20)
# print(rmd)


   #Case 1
   
A= string.digits
B= string.ascii_uppercase
C= string.ascii_lowercase
D= string.punctuation
# random.shuffle(A)
# random.shuffle(B)
# random.shuffle(C)

punc= random.sample(D,2)
dig= random.sample(A,4)
Lower=random.sample(C,9)
Upper = random.sample(B, 1)
password= Upper + Lower + dig + punc
   
print("".join(password))

#Case 2
# from random import randint

# num= [] 
# for i in range(17):
#     num.append(randint(1,17))
# print(num)


# import string
# import random
# def password():
#     a = random.randint(1,17)
#     newpassword= []
#     newpassword.append(a)
#     print(newpassword)
#     while len(newpassword)<=17:
#         for x in a:
#             return newpassword
# password()    

# print(chr(97))

# import random
# import string

# def get_random_alphanumeric_string(length):
#     letter_and_digits= string.ascii_letters + string.digits
#     result_str= "".join((random.choice(letter_and_digits)for i in range(length)))
#     print('suggested password:', result_str)
# get_random_alphanumeric_string(15)
    
    

