# a=11**0
# print(a)
# a=11**1
# print(a)
# a=11**2
# print(a)
# def pascal(*values):
#     a=11
#     for x in values:
#       a=(a**x) 
#     return a
# print(pascal(1,2))

# n=int(input('Enter your number'))
# listme= []
# for x in range(n):
#     list_me= []
#     for y in range (x+1):
#         if y==0 or y==x:
#             list_me.append(1)
#         else:
#             list_me.append(listme[x-1][y-1] + listme[x-1][y])
#     listme.append(list_me)
# print()
        
# def combine(n):
#     for x in range(n+1):
#         for y in range(n-x):
#             print(' ', end='')
                
#         z = 1
#         for y in range(1, x+1):
#             print(z,' ', sep='', end='')
#             z = z*(x - y) // y
#         print()
            
# n = 4
# combine(n)

# ######
# from math import factorial
# n = int(input('Enter the value of n'))
# while (n > 0):
#     n = n-1
#     r = 0
#     while (r<=n):
#         s = factorial(n)
#         y = factorial(n-r)
#         z = factorial(r)
#         b = (s)/(y*z)
#         r = r + 1
#         print(b)
#     print('xxxxxxxxxxx')

x = ['rice', 2, 3, 4, 4, 'goat', 5, 6, 7, 1, 8, 'garri', 10]
print(x[:13:3])

