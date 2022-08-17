import datetime as dt
from time import sleep          



# today = dt.datetime.today()
# r=dt.date.strftime(today,'%y')
# print(r)

myDate = 'Sun August, 2022'
# print(dt.datetime.strptime(myDate,'%a %B, %Y'))
# print(dt.date(2011,12,12))
# today = dt.date.today().month

# newDate = dt.date(2022, 8,23).year
# diff = newDate + 2
# t1=dt.timedelta(minutes=50,seconds=10)
# t2 = dt.timedelta(minutes=40,seconds=50)
# print(t1 + t2)
# sleep(5)
# print('I am done')

# mytime = dt.datetime.now()
# mytimef= dt.datetime.strftime(mytime,'%I:%M:%S%p')

# while (True):
#     print(mytime)
#     sleep(1)

lst = ['Ade', 'Toyin', 'Bimbo', 'Tope', 'Ola']
i =len(lst)-1
while (i >= 0):
    print(lst[i]*2)
    i-=1