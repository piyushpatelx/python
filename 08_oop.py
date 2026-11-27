#1 multilevel inheritance
class Vehicle:
    def start(self):
        print("vehicle start")

class Car(Vehicle):
    def drive(self):
        print("car driving")

class ElectricCar(Car):
    def charge(self):
        print("charging")

e=ElectricCar()
e.start()
e.drive()
e.charge()


#2 multiple inheritance
class Teacher:
    def teach(self):
        print("teaching")

class Researcher:
    def res(self):
        print("researching")

class Professor(Teacher,Researcher):
    def work(self):
        print("professor working")

p=Professor()
p.teach()
p.res()
p.work()


#3 hierarchical inheritance
class Shape:
    def show(self):
        print("shape")

class Circle(Shape):
    def area(self,r):
        print("circle area:",3.14*r*r)

class Rectangle(Shape):
    def area(self,l,b):
        print("rect area:",l*b)

class Triangle(Shape):
    def area(self,b,h):
        print("tri area:",0.5*b*h)

c=Circle()
c.area(5)
r=Rectangle()
r.area(4,5)
t=Triangle()
t.area(3,6)


#4 method overriding
class Animal:
    def sound(self):
        print("animal sound")

class Dog(Animal):
    def sound(self):
        print("bark")

class Cat(Animal):
    def sound(self):
        print("meow")

d=Dog()
c=Cat()
d.sound()
c.sound()


#5 operator overloading
class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,o):
        return Complex(self.r+o.r,self.i+o.i)

    def show(self):
        print(self.r,"+",self.i,"i")

c1=Complex(2,3)
c2=Complex(4,5)
c3=c1+c2
c3.show()


#6 private variable
class Emp:
    def __init__(self,name,sal):
        self.name=name
        self.__salary=sal

    def show(self):
        print(self.name,self.__salary)

e1=Emp("rahul",40000)
e1.show()


#7 atm encapsulation
class ATM:
    def __init__(self,pin,bal):
        self.__pin=pin
        self.__bal=bal

    def check(self,p):
        if p==self.__pin:
            print("balance:",self.__bal)
        else:
            print("wrong pin")

    def withdraw(self,p,amt):
        if p!=self.__pin:
            print("wrong pin")
        elif amt>self.__bal:
            print("not enough balance")
        else:
            self.__bal=self.__bal-amt
            print("withdrawn, left:",self.__bal)

a=ATM(1234,10000)
a.check(1234)
a.withdraw(1234,2000)


#8 game character
class Character:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp

    def info(self):
        print(self.name,"hp:",self.hp)

class Warrior(Character):
    def attack(self):
        print(self.name,"sword attack")

class Mage(Character):
    def attack(self):
        print(self.name,"fireball")

w=Warrior("arjun",120)
m=Mage("sam",90)
w.info()
w.attack()
m.info()
m.attack()