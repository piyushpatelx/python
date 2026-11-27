#1 factorial using loop
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

print("fact =",fact(5))


#2 sum of n natural numbers
def nsum(n):
    if n==0:
        return 0
    return n+nsum(n-1)

print("sum =",nsum(10))

#3 reverse string using recursion
def rev(s):
    if len(s)==0:
        return
    print(s[-1],end="")
    rev(s[:-1])

rev("hello")
print()


#4 power x^n
def pwr(x,n):
    if n==0:
        return 1
    return x*pwr(x,n-1)

print("power =",pwr(2,5))