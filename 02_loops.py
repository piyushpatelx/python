#1 automorphic number
n=int(input("enter number: "))
sq=n*n
t=n
flag=1
while t>0:
    if t%10 != sq%10:
        flag=0
        break
    t=t//10
    sq=sq//10

if flag==1:
    print("automorphic")
else:
    print("not automorphic")


#2 palindrome range
a=int(input("start: "))
b=int(input("end: "))
for i in range(a,b+1):
    t=i
    rev=0
    while t>0:
        d=t%10
        rev=rev*10+d
        t=t//10
    if rev==i:
        print(i,end=" ")
print()

#3 lcm and hcf
x=int(input("first num: "))
y=int(input("second num: "))
if x<y:
    m=x
else:
    m=y

hcf=1
for i in range(1,m+1):
    if x%i==0 and y%i==0:
        hcf=i

lcm=max(x,y)
while True:
    if lcm%x==0 and lcm%y==0:
        break
    lcm=lcm+1

print("hcf =",hcf)
print("lcm =",lcm)


#4 password retry
cp="admin123"
cnt=0
while cnt<3:
    p=input("enter password: ")
    if p==cp:
        print("login done")
        break
    else:
        cnt=cnt+1
        print("wrong pass")
if cnt==3:
    print("blocked")


#5 star patterns
n=5
print("triangle")
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

print("pyramid")
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)

print("diamond")
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i) + "* "*i)