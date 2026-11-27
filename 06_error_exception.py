#1 age validation
try:
    age=int(input("enter age: "))
    if age<18:
        raise Exception("age is less than 18")
    print("valid age")
except Exception as e:
    print(e)


#2 bank withdrawal
bal=5000
try:
    amt=int(input("enter withdraw amount: "))
    if amt>bal:
        raise Exception("low balance")
    bal=bal-amt
    print("done, left balance:",bal)
except Exception as e:
    print(e)


#3 password validator
class LenErr(Exception):
    pass
class UpperErr(Exception):
    pass
class NumErr(Exception):
    pass

try:
    pw=input("enter password: ")
    if len(pw)<8:
        raise LenErr("length less than 8")

    u=0
    num=0
    for ch in pw:
        if ch.isupper():
            u=1
        if ch.isdigit():
            num=1

    if u==0:
        raise UpperErr("no uppercase letter")
    if num==0:
        raise NumErr("no number in password")

    print("password ok")
except LenErr as e:
    print(e)
except UpperErr as e:
    print(e)
except NumErr as e:
    print(e)