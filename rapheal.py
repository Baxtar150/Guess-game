
# # # from cgi import print_arguments


# name='ojo'
# age=23
# maritalstatus='single'
# result='my name {0} i am {1} years old.i am {2}'

# print(result.format(name,age,maritalstatus))

# # # mylist =['ojo','bright','timmy']
# # # for li in mylist:
# # #     print(li)
 
# # # print (type(mylist))
# # # meg='i love myseif anyhow'
# # # print('lover'in meg)
# # # if ('lover') in meg:
# # #     print('found')
# # # else:
# # #     print('not found')


# # # print
# # from bisect import bisect_right


# # odd_List = [1, 3, 5, 7]
# # even_Tuple = (2, 4, 6, 8, 10)
# # print(odd_List, even_Tuple)

# bright= ['book', 2.2, 10, True, 'Food']
# bimbo= {'food':'rice', 3:'three', 'phone':'call'}
# print(bright, bimbo)

# day=23
# month= 'July'
# year= 2022
# print(day, month, year, sep="-")

# bright=[2, 4, 5, 7, 9]
# for i in bright:
#     print(i**5, end="-")
# print(bright)

# 9
# # for and operator, both conditions 
# F=3
# G=7
# R= F&G
# print(R)

# a = [1,2,3,4,5]
# b = [6,7,8]
# a.extend(b)

# print(a)

# result=a.copy()
# print(result)
# print(a is result)#The comparism of data affects the subjects(variable)
# print(a==result)#The comprism of data affects the object(content)

# names=['Ojo', 'Dada', 'Joshua', 'Tolani', 'Mosun']
# for x in names:
#     print(x)
    
# names=['Ojo', 'Dada', 'Joshua', 'Tolani', 'Mosun']
# if (x=='Ojo'):
#     print(x)
  


# age = int(input('enter your age'))
# print(age)

# if (age >= 18):
#     print('you are allowed to vote')
# else:
#     print('You are not allowed to vote')
    
# names=['Ojo', 'Dada', 'Gbenga', 'Bosede', 'Joshua', 'Tolani', 'Ronke', ]

#  
# score = int(input('Enter your score'))
# print(score)

# if (score>= 75):
#     print ('A')
# elif(score >=65 and score< 75):
#     print('B')
# elif (score >=55 and score <65):
#     print('C')
# elif(score >=45 and score <55):
#     print('D')
# elif(score >=40 and score <45):
#     print('E')
# else:
#     print('F')


# list=['moimoi', 'garri', 'plate', 'spoon', 'cup']
# for x in list:
#     if (x=='plate'):
#         continue
# print(x)

# list=['moimoi', 'garri', 'plate', 'spoon', 'cup']
# tr=['singlet', 'phone', 'book']
# list.extend(tr)
# print(list) 

# [print(x.upper()) for x in list]

# variable = 'damilola', "damilola" string
# variable = 23 int
#             23.0  float 

# from ast import Global
# from calendar import LocaleHTMLCalendar


# VARIABLE = "JGF"
# print(VARIABLE)

# vari_able= 45
# footwear='slipper', 'boot', 'sandal'
# FOOTWEAR= 'slipper', 'boot', 'sandal'
# footWear= 'slipper', 'boot', 'sandal'
# footWear= 'slipper', 'boot', 'sandal'
# FootWear= 'slipper', 'boot', 'sandal'
# foot_wear= 'slipper', 'boot', 'sandal'

# footwear="sandal"
# print(True) boolean

# boy = 46
# girl = 30
# gender= boy / girl 
# print('The answer is', gender)

# x= 56
# y= 20   
# answer= x+y*y/x-y+x

# print(answer)
# if 105 > (answer):
#     print('good')
# else:
#     print('bad')

# Variable scope:
#     Global
#     Local 

# x= 20


# def me():
#     global x
#     x= 60
#     print(x)
# me()
# print(x)


# z= 31
# def me():
#     global z
#     z=50
#     print(z)
# me()
# print(z)


# print(12)
# a=int(12)
# print(a), print(float(12))

# print(12.3)
# b=int(12.3)
# print(b)

# # c= a+b
# # print(c)


# d= float(12)
# print(d)

# e= d + a 
# print(e)


# from re import A


# age= 20
# name= 'Jide'
# print("Hello," + name +" "+ "you are" + " "+ str(age) + "years old")

# a=5
# b=3
# c= a|b
# print(c)

# from calendar import c
# from math import factorial
# import numbers


# rapheal=[]
# you=['muritala', 'Omobolaji', 'Ayo']
# rapheal.append(you)
# print(rapheal)

# me=['Taylor', 50]
# rapheal.extend(me)
# print(rapheal)

  
# names=['Ojo', 'Dada', 'Joshua', 'Tolani', 'Mosun', 'apple', ]
# [print(x.upper()) for x in names if x=='Dada']
# #Expression, looping and condition
#looping will pick each item in the list and start all over again until the number of item required is attended to.


# *Comprehensional expression must have a sqaure bracket 
# Expression, Looping, Condition
# [print(x.upper()) for x in names if 'a' in x]
# The condition (if 'a' in x means look for all values with a in them and )



# food=['Rice', 'Beans', 'Amala', 'Pounded yam', 'Bread', 'Meat', 'Egg', 'Coconut']
# [print(x.upper()) for x in food if x==x]
# drink=['Coke', 'Fanta', 'Water', 'Malt']
# footBallers=['Messi', 'Ronaldo', 'Mane', 'Salah']
# ()----Turple
# []---- LIst
# {}-----Dictionary and set


# food.extend(footBallers)
# print(food)

# food.append(drink)
# print(food)

# food=['Rice', 'Beans', 'Amala', 'Pounded yam', 'Bread', 'Meat', 'Egg', 'Coconut']
# [print(y.upper()) for y in food if y==y]


# food=['Rice', 'Beans', 'Amala', 'Pounded yam', 'Rice', 'Bread', 'Meat', 'Egg', 'Coconut', 'coconut']

# if 'Amala' in food:
#     print('correct')
# elif 'Rice' in food:
#     print(True)
# elif 'Eba' in food:
#     print('correct')
# else:
#     print('incorrect')

# names=('Ojo', 'Clara', 'Adeolu', 'Joshua', 'Johnson','Abosede')
# result=names[3:len(names)]#The [] in this case is used as an arrary to call a range/ to assess a sub item from the main item
# print(len(names))
# print(names.count('Ojo'))
# print(names.index('Johnson'))
# print(result)

# #tuple can be changed by first converting to list then manipulate and change back to tuple/replaced or deleted..
# newlist=list(names)
# newlist[1]= "Rebecca"
# print(tuple(newlist))

# newlist.append('Fish')
# print(tuple(newlist))

# newlist.remove('Joshua')
# print(tuple(newlist))

# [print(x.upper()) for x in newlist if 'b' in x or 'B' in x]# the  condition if "b" or "B" is used to located the valve in each item
# # Question
# # create a collection, a 1-10, print it in colounm, if the item is 5 break collection
# bright=[1,2,3,4,5,6,7,8,9,10]
# for x in bright:
#     if (x==5):
#         break
    
#     print(x)
#     write a prog that will ask users to enter a number that will ask the users to generate factorial of a numbers
# x=int(input('Enter Number'))
# for y in x:
#     if (y==(n(n-1,n-2,))):
#         print(x)
# factorial= 1
# number= int(input('Enter your value of factorial'))
# if(number< 0):
#     print('It is not valid')
# elif(number== 0):
#     print("factorial of 0 is 0")
# elif(number==1):
#     print("factorial of 1 is 1")
# else:
#     for x in range(1, number + 1):
#         factorial= factorial * x
#     print(factorial)  
 
#  Quadratic equati
# import math
# a=2
# b=4
# c=2
# determinant= (b**2) - 4*a*2
# if (determinant < 0):
#     print('it is a complex root')
# elif(determinant ==0):
#     x1 = ((-b) +  math.sqrt(determinant))/2*a
#     print(x1)
# else:
#     x1 =((-b) + math.sqrt(determinant))/2*a
#     x2 =((-b) - math.sqrt(determinant))/2*a
#     print(x1, x2)
    
# name = list(input("Enter a word: "))
# comapp = name.copy()
# comapp.reverse()
# if name == comapp:
#     print("It is palindrone ")
# else:
#     print("it is not working")


# x = str(input('Enter a word:'))
# y= x.copy()
# y.reverse()
# if x== y:
#     print('It is a palindrome')
# else:
#     print('it is not')
    
# a = str(input('Enter a word:'))
# b= a.lower
# c=list(a.lower)
# d=c.copy()
# e=d.reverse()
# f= str(e)
# if f== a:
#     print('It is a palindrome')
# else:
#     print('it is not')

# word= list(str.lower(input('Enter your word')))
# reverse= word.copy()
# print(reverse)
# [print(f)]

# def ispalindrome(word):
#     return word== word[::-1]

# mywords = str.lower(input('Enter your word'))

# if(ispalindrome(mywords)):
#     print('It is a palindrome')
# else:
#     print('It is not a palindrome')


#SET: is the opposite of 'list': cant be duplicated, not ordered, unchangable.
#used for mathematical function: 
#uses {}curly bracket

# myset= {1,2,3,4,5,6,"me","fish"}
# print(myset)

# pi=float(3.142)
# r=input("radius of a circe")
# area= pi* float(r)**2
# print(area)

# import math
# pi= math.pi
# r= float(input('raddius'))
# #pr2
# answer=pi*r**2
# print(f'Answer for {r} radius is {answer}')

# from ast import operator


# from email.errors import FirstHeaderLineIsContinuationDefect




# first= float(input('Enter first number:'))
# second= float(input('Enter second number'))
# Third= input('Enter operator')
# signs= ['+', '-', '*', '/']
# for x in signs:
#     a= first + second
#     print (a)


# def calculate():
#     operation = input('''
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')
# number_1 = int(input('Please enter the first number: '))
# number_2 = int(input('Please enter the second number: '))

# if operation == '+':
#     print('{} + {} = '.format(number_1, number_2))
#     print(number_1 + number_2)

# elif operation == '-':
#     print('{} - {} = '.format(number_1, number_2))
#     print(number_1 - number_2)

# elif operation == '*':
#     print('{} * {} = '.format(number_1, number_2))
#     print(number_1 * number_2)

# elif operation == '/':
#     print('{} / {} = '.format(number_1, number_2))
#     print(number_1 / number_2)

# else:
#     print('You have not typed a valid operator, please run the program again.')


# Assignment 3
# first= float(input('Enter first number:'))
# second= float(input('Enter second number'))
# Third= input('Enter operator')


# def calculate(first, second, third):
#         if third== '+':
#             a=first + second
#             print (a)
#         elif (third == '-'):
#             a=first - second
#             print (a)
#         elif (third == '*'):
#             c=first * second
#             print (c)
#         elif (third == '/'):
#             d= first / second
#             print (d)
#         else:
#             return 'You entered an invalid operator'
    
# answer = calculate(first, second, Third)
# print(answer)

# from ast import operator

#Assignment 1
# first= float(input('enter first number:'))
# second= float(input('enter second number'))
# third=input('enter operator')

# for x in third:
#     if third =='+':
#         add=first + second
#         print(add)
#     elif third =='-':
#         subtract=first - second
#         print(subtract)
#     elif third =='*':
#         multiply=first * second
#         print(multiply)
#     elif third =='/':
#         divide=first / second
#         print(divide)

# evennumber= 2
# while (evennumber <= 50):
   
#     x= evennumber + 2
#     print (x)

# from re import A


# start, end=1, 50

# for num in range(start, end + 1):
#     if num % 2==0:
#         print(num, end= " ")

# Assignment 2
# # list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

        
# even_nos = list(filter(lambda x: (x % 2 == 0), list2))
 
# print("Even numbers in the list: ", even_nos)

# list2 = range(52)
# for x in list2:
#     if x % 2==0:
#         print(x)

# def Even(number):
#     for x in range(number+ 1):
#         print(x)
#         x+=2
# Even(4)
        
# #Dictionary
# student={}
# student= {'name':'Ojo', 'subject':['maths','English'], 1:4, 'ismarried':True} #{'Key':'Value'}pair.  Value can be of any data type
# scores={}
# print(student)
# print(student['subject'])#to get the value of a particular key
# #Get methods helps access a value from its key by bypassing the key
# print(student.get(' '))

# employee={
#     'junior':{'name':'Olatunji', 'age':13, 'status':'single', 'salary':'34000'},
#     'senior':{'name':'Ade', 'age':40, 'status':'married', 'salary':90000}}

# print(employee)
# for emp in employee:
#     if emp=='senior':
#         print(emp)
#         for x in employee(emp).keys():
#             print(x)
        
# Tobi={'food': 'rice', 'cars':'toyota', 'birds':'parrot', 'number':2}
# bright={}.fromkeys(Tobi)
# print(bright)
# bright['food']='beans'
# bright['cars']='honda'
# bright['birds']='bat'
# bright['number']= 6
# bimbo= bright.keys
# print(Tobi.keys)

# import random

# A={'A', 'B', 'C', 'D', 'E', 'F'}
# a={'a', 'b', 'c', 'd', 'e', 'f'}
# num={1,2,3,4,5,6,7,8,9,0}
# chars={'!', '@', '#', '$', '5' '6'}

# b=random.randint(num)

