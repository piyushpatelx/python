#1 palindrome string
s=input("enter string: ")
s=s.replace(" ","").lower()
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#2 longest word
st=input("enter sentence: ")
w=st.split()
big=""
for i in w:
    if len(i)>len(big):
        big=i
print("longest word:",big)


#3 anagram check
a=input("str 1: ").replace(" ","").lower()
b=input("str 2: ").replace(" ","").lower()
if sorted(a)==sorted(b):
    print("anagram")
else:
    print("not anagram")


#4 remove duplicate chars
s=input("enter string: ")
ans=""
for ch in s:
    if ch not in ans:
        ans=ans+ch
print("output:",ans)

#5 compress string
s=input("enter string: ")
res=""
c=1
for i in range(len(s)):
    if i+1<len(s) and s[i]==s[i+1]:
        c=c+1
    else:
        res=res+s[i]+str(c)
        c=1
print(res)