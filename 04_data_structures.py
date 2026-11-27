#1 list rotation
l=[1,2,3,4,5]
k=int(input("enter k: "))
d=input("left or right: ")
k=k%len(l)
if d=="left":
    ans=l[k:]+l[:k]
else:
    ans=l[-k:]+l[:-k]
print(ans)


#2 remove duplicates without set
a=[1,2,2,3,4,3,5,1]
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)

#3 missing number
arr=[1,2,3,5,6]
n=len(arr)+1
s1=n*(n+1)//2
s2=0
for x in arr:
    s2=s2+x
print("missing:",s1-s2)


#4 tuple subjects
sub=("maths","physics","python","english","chemistry")
print("3rd subject:",sub[2])
print("total:",len(sub))
print("index of python:",sub.index("python"))


#5 tuple to dict
t=((1,"A"),(2,"B"))
d={}
for x in t:
    d[x[0]]=x[1]
print(d)


#6 swap first and last using tuple unpacking
t=(10,20,30,40,50)
a,*mid,b=t
t2=(b,*mid,a)
print(t2)


#7 subset check
s1={1,2,3}
s2={1,2,3,4,5}
if s1.issubset(s2):
    print("yes subset")
else:
    print("not subset")


#8 student marks analyzer
marks={"amit":78,"rohit":91,"neha":28,"raj":64,"pooja":30}
top=""
mx=-1
tot=0
fail=[]

for k in marks:
    v=marks[k]
    tot=tot+v
    if v>mx:
        mx=v
        top=k
    if v<33:
        fail.append(k)

print("topper:",top,mx)
print("average:",tot/len(marks))
print("failed:",fail)


#9 library management
lib={"python":3,"java":2,"c":5}
print("books:",lib)
b=input("book to issue: ")
if b in lib and lib[b]>0:
    lib[b]=lib[b]-1
    print("issued")
else:
    print("not available")

r=input("book to return/add: ")
if r in lib:
    lib[r]=lib[r]+1
else:
    lib[r]=1
print("updated:",lib)