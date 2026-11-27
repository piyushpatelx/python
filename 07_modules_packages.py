#1 math module
import math
print("sqrt:",math.sqrt(25))
print("pow:",math.pow(2,3))
print("fact:",math.factorial(5))
print("sin 90:",math.sin(math.radians(90)))
print("cos 0:",math.cos(math.radians(0)))


#2 random module
import random
otp=random.randint(1000,9999)
print("otp:",otp)

ch="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
pw=""
for i in range(8):
    pw=pw+random.choice(ch)
print("pass:",pw)

lst=[]
for i in range(5):
    lst.append(random.randint(1,50))
print("list:",lst)


#3 datetime module
import datetime
now=datetime.datetime.now()
print("now:",now)
yr=int(input("enter birth year: "))
print("age:",now.year-yr)


#4 geometry package
from geometry import circle,rectangle
print("circle area:",circle.area(5))
print("circle circum:",circle.circum(5))
print("rect area:",rectangle.area(4,6))
print("rect peri:",rectangle.peri(4,6))