# Electricity Bill Program

m = int(input("Enter current meter number: "))
bill = 0.0
if( m == 1234):
   pass
print("1-Agricultural")
print("2-Residential")
print("3-Commercial")
c = int ( input ( "Choose Category: " ))
if (c == 1):
 s = 20;
u = int(input("Enter number of units consumed: "))
if (u > 0 and u < 50):
    bill = (u * 0.25) + s;
elif (u >= 50 and u < 150):
    bill = (u * 0.55) + s
elif (u >= 150 and u < 300):
    bill = (u * 0.80) + s
elif (u >= 300 and u <500):
    bill = (u * 1) + s
elif (u >= 500 and u<1000 ):
    bill = (u * 2) + s
else:
    print("Invalid Units")
    print("Current meter number: ",m)
    print("Number of units consumed: ",u)
    print("Selected Category: ",c)
    print("Your bill amount: %.2f"%bill)
if(c == 2):
    s = 35;
    u = int(input("Enter number of units consumed: "))
if (u > 0 and u < 50):
    bill = (u * 1.35) + s;
elif (u >= 50 and u < 150):
    bill = (u * 2.15) + s
elif (u >= 150 and u < 300):
    bill = (u * 3) + s
elif (u >= 300 and u < 500):
    bill = (u * 3.5) + s
elif (u >= 500 and u<1000):
    bill = (u * 6) + s
else:
    print("Invalid Units")
    print("Current meter number: ", m)
    print("Number of units consumed: ", u)
    print("Selected Category: ", c)
    print("Your bill amount: %.2f" % bill)
if(c== 3):
    s = 65;
u = int(input("Enter number of units consumed: "))
if (u > 0 and u < 50):
    bill = (u * 3) + s;
elif (u >= 50 and u < 150):
    bill = (u * 4.5) + s
elif (u >= 150 and u < 300):
    bill = (u * 5.5) + s
elif (u >= 300 and u <500):
    bill = (u * 6.8) + s
elif (u >= 500 and u<1000 ):
    bill = (u * 9) + s
else:
    print("invalid Units")
    print("Current meter number: ", m)
    print("Number of units consumed: ", u)
    print("Selected Category: ", c)
    print("Your bill amount: %.2f" % bill)
    
    pass
if(c==4):
    print("Wrong choice")
else:
    print("Wrong pin number")