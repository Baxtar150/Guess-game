# class student:
#     def __init__(self, name, age, sex):
#         self.name= name
#         self.age= age
#         self.sex= sex
        
#     def getName(self):
#         return self.name
    
#     def getAge(self):
#         return self.age
    
#     def getSex(self):
#         return self.sex
    
#     def getRecords(self):
#         return list(self.name, self.age, self.sex)
    
#     def deleteRecords(self):
#         del self.name
#         del self.age
#         del self.sex
        
#     def ToUpper(text):
#         return text.toUpper()
    
# std= student('Adedoyin', 27, 'Female')
# print(std.getRecords())
    
# class python:
#     store =[]
#     def __init__(self, place, vehicle, fruit):
#         self.Place = place
#         self.Vehicle = vehicle
#         self.Fruit = fruit
        
#         self.store.append(self.Place)
#         self.store.append(self.Vehicle)
#         self.store.append(self.Fruit)
        
#     def getRecord(self):
#         return self.store

# obj = python("ekiti", "Maybach", "Apple")
# print(obj.getRecord())

# a= obj.getRecord()
# for x in a:
#     print(x)

word= "    my name is rapheal"
print(word.lstrip())