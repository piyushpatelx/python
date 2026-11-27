#1 electricity bill
u=int(input("enter units: "))
if u<=100:
    bill=u*5
elif u<=300:
    bill=100*5 + (u-100)*7
else:
    bill=100*5 + 200*7 + (u-300)*10

if bill>2000:
    bill=bill + bill*0.05
print("total bill =",bill)


#2 loan approval
sal=int(input("enter salary: "))
cs=int(input("enter credit score: "))
age=int(input("enter age: "))

if sal>=25000 and cs>=700 and age>=21 and age<=60:
    print("Approved")
elif age>=21 and age<=60 and (sal>=25000 or cs>=700):
    print("Conditionally Approved")
else:
    print("Rejected")

#3 number check
n=int(input("enter number: "))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")

if n%2==0:
    print("even")
else:
    print("odd")

if n%3==0 and n%5==0:
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")


#4 exam result
m1=int(input("sub 1 marks: "))
m2=int(input("sub 2 marks: "))
m3=int(input("sub 3 marks: "))
m4=int(input("sub 4 marks: "))
m5=int(input("sub 5 marks: "))

if m1<33 or m2<33 or m3<33 or m4<33 or m5<33:
    print("Fail")
else:
    p=(m1+m2+m3+m4+m5)/5
    print("percentage =",p)
    if p>=60:
        print("First division")
    elif p>=50:
        print("Second division")
    elif p>=40:
        print("Third division")
    else:
        print("Pass")