# # def sayhello():
# #     a = 2
# #     while (a>0):
# #         if a==2:
# #             print("the sum is "+ str(a))
# #         sayhello()
# #         a = a - 1


# # result = sayhello()
# # print(result*2)

# x = lambda a , b : a * b
# print(x(4, 5))


# class Ben:
#     def sayname(name):
#         return "Your name is "+name


# nums = int(input("Enter the total number of students"))
# start = 1
# while start <= nums:
#     name = input("Enter your name: \n")
#     person = Ben.sayname(name)
#     print(person)
#     start = start + 1



# class Ageman:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def sayname(self):
#         return "Your name is "+self.name

# myageman = Ageman("Samuel",12)
# print(myageman.sayname())


# class Showage:
#     def __init__(self,firstname,othername,year):
#         self.firstname = firstname
#         self.othername = othername
#         self.age = 2022 - year
#     def theconstructor(self):
#         return "Your names are "+self.firstname+" "+self.othername+" and your age is "+ str(self.age)

# firstname = input("Enter Your firstname \n")
# othername = input("Enter your othername \n")
# year = int(input("Enter your year of birth \n"))

# person = Showage(firstname,othername,year)

# print(person.theconstructor())


# class Showage:
#     def __init__(self,firstname,othername,year):
#         self.firstname = firstname
#         self.othername = othername
#         self.age = 2022 - year
#     def theconstructor(self):
#         return "Your names are "+self.firstname+" "+self.othername+" and your age is "+ str(self.age)
# i = 1
# while i <= 3: 
#     firstname = input("Enter Your firstname \n")
#     othername = input("Enter your othername \n")
#     year = int(input("Enter your year of birth \n"))

#     person = Showage(firstname,othername,year)

#     print(person.theconstructor())
#     i = i + 1


# class Showage:
#     def __init__(self,firstname,othername,year):
#         self.firstname = firstname
#         self.othername = othername
#         self.year = year
#         self.age = 2022 - year
#     def theconstructor(self):
#         return "Your names are "+self.firstname+" "+self.othername+" and your age is "+ str(self.age)
#     def theage(self):
#         self.age = 2022 - self.year
#         return self.age


# class Babydrive(Showage):
#     def __init__(self,firstname,othername,year):
#         super().__init__(firstname,othername,year)
#     def babydrive(self):
#         if(super().theage()>=18):
#             return "You are elligible to vote"
#         else:
#             return "You are too young to vote"

# baby = Babydrive("Michael","Gabriel",2000)
# print(baby.theconstructor() + "\n" +   baby.babydrive())

# class MyClass:
#     x = 10
# # print(MyClass)
# Obj = MyClass()
# print(Obj.x)

# class David:
#     def __init__(self,name,gender,age):
#         self.name = name
#         self.gender = gender
#         self.age = age
    
# Obj = David("Michael","male", 16)

# Obj.age = 30
# Obj.name = "Gabriel"
# print(Obj.name)
# print(Obj.gender)
# print(Obj.age)


# class David:
#     def __init__(self,name,gender,age):
#         self.name = name
#         self.gender = gender
#         self.age = age
#     def myfunc(self):
#         print("Hi my name is " + self.name)
#         print("Hi my name is "+ self.name,"I am a " + self.gender,)
#         print("I am ",str(self.age), "years old")
#         print("Hi, Happy New Month, my name is "+ self.name, "I am a " + self.gender, "and I am ",str(self.age), "years old")
# Obj = David("Michael",'male', 16)
# Obj.myfunc()

# class Solomon(David):
#     def __init__(self,name,gender,age):
#         super().__init__(name,gender,age)
#     def solomon(self):
#         if(super().age()>=8):
#             return "You must go on evangelism"
#         else:
#             return "You are too young"

# slm = Solomon("Michael","male",16)
# print(slm.myfunc() + "\n" +   slm.solomon()) 