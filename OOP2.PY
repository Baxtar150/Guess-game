class python:
    store =[]
    def __inti__(self, place, vehicle, fruit):
        self.Place = place
        self.Vehicle = vehicle
        self.Fruit = fruit
        
        self.store.append(self.Place)
        self.store.append(self.Vehicle)
        self.store.append(self.Fruit)
        
    def getRecord(self):
        return self.store# returns the total of all self.store.append
    
obj= python("Ekiti", "Maybach", "Apple")
print(obj.getRecord())

# for rec in obj.getRecord():
#     print(rec)

# INHERETANCE
# class Boy:
#     __eyes=2 putting double underscore make a property private.
#     eyes=2
#     nose=1
#     def __init__(self):
#         self.age =30
    
#     def run(self):
#         print('you can run')
#     def dance(self):
#         print('You can dance')
    
#     def getEyes(self):
#         return self.eyes
#         return self.__eyes
    
# class Girl(Boy):# the bracket(Boy) is used to inheret the properties of Boy 
#     def __init__(self):
#         pass
        
#     def breastFeed(self):
#         print('you can breastfeed')
#     def reproduce(self):
#         print('you can reproduce')

# human= Girl()
# human.breastFeed()
# human.dance()   
# boy = Boy()
# print(boy.getEyes())
        
        
        
# ITERATION
# class Num():
#     def __iter__(self):
#         self.a =1
#         return self
    
#     def __next__(self):
#         if (self.a < 5):
#             b=self.a
#             self.a =self.a + 1
#             return b
#         else:
#             StopIteration
    
# obj= Num()
# itr= iter(obj)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
        
        

        



