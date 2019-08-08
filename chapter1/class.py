#!/Users/huan/anaconda3/bin/python
# coding=utf-8
'''
class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def color(self, color):
        print("%s is %s" %(self.name, color))
boy=Person("liuhuan")
boy.color("Blue")
class A():
    x=7
print(A.x)
foo = A();
foo.x +=1
print("foo.x %s A.x %s" %(foo.x,A.x))
del foo.x
print(foo.x)
foo.y=100
print(foo.y)

class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def color(self, color):
        print("%s is %s" %(self.name, color))
    def how(self):
        print("%s breast " %(self.name))

girl= Person("DuanCongMin")
girl.color("White")
girl.how()
'''
'''
class Person:
    def speak(self):
        print("I love you.")
    def setHeight(self):
        print("The height is:1.60m.")
    def breast(self, n):
        print("My breast is: ", n)
    def eyes(self):
        print("Two eyes")

class Girl():
    age = 28
    def color(self):
        print("The girl is white")
    def setHeight(self):
        print("The height is: 1.70m.")
class HotGirl(Girl, Person):
    pass
'''
'''
class Person:
    def __init__(self):
        self.height = 160
    def about(self, name):
        print("{} is about {}".format(name, self.height))
class Girl(Person):
    def __init__(self):
        super(Girl, self).__init__()
        self.breast=90
    def about(self,name):
        print("{} is a hot girl, she is about {}, and her breast is {}".format(
            name, height, breast
        ))
        super(Girl, self).about(name)

class people:
    name=''
    age=0
    __weight=0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight=w
    def speak(self):
        #print("%s:我 %d 岁."%(self.name, self.age))
        print("%s:我 %d 岁" % (self.name, self.age))
    def getWeight(self):
        return self.__weight
class student(people):
    grade=''
    def __init__(self, n, a, w, g):
        super(student,self).__init__( n, a, w)
        self.grade=g
    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年级, 体重 %d "%(self.name, self.age,self.grade, self.getWeight()))
class StaticMethod:
    @staticmethod
    def foo():
        print("This is static method foo()")
class ClassMethod:
    @classmethod
    def bar(cls):
        print("This is class method bar()")
        print("bar() is part of class:",cls.__name__)
def length(x):
    print("The length of ", repr(x), " is ", len(x))
class Animal:
    def __init__(self, name=""):
        self.name = name
    def talk(self):
        pass
class Cat(Animal):
    def talk(self):
        print("Meow")
class Dog(Animal):
    def talk(self):
        print("Woof")
def duotai(animal):
    animal.talk()
class ProtectMe:
    def __init__(self):
        self.me="liuhuan"
        self.__name="liu"
    def __python(self):
        print("I love Python.")
    def code(self):
        print("Which language do you like?")
        self.__python()
    @property
    def name(self):
        return self.__name
class Rectangle:
    def __init__(self):
        self.width=0
        self.length=0
    def setSize(self, size):
        self.width, self.length = size
    def getSize(self):
        return self.width, self.length
    size = property(getSize, setSize)
class NewRectangle:
    def __init__(self):
        self.width=0
        self.length=0
    def __setattr__(self, name, value):
        print("__setattr__")
        if name == "size":
            self.width, self.length=value
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
        print("__getattr__")
        if name == "size":
            return self.width, self.length
        else:
            raise AttributeError
'''
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index=len(data)
    def __iter__(self):
        return self
  
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
def fibs(max):
    n, a, b= 0, 0, 1
    while n < max:
        yield(b)
        a,b=b,a+b
        n += 1
'''
while True:
    print("This is a division program.")
    c=input("Input 'c' continue, otherwise logout:")
    if c=='c':
        a=input("First number:")
        b=input("Second number:")
        try:
            print(float(a)/float(b))
            print("*****************************")
        except ZeroDivisionError:
            print("The second number can't be zero!")
            print("******************************")
    else:
        break

class Calculator:
    is_raise=False
    def calc(self, express):
        try:
            return eval(express)
        except (ZeroDivisionError, ValueError):
            if self.is_raise:
                #print("Zero can not be divesion")
                #print(e)
                print("***************************")
            else:
                raise
b = Calculator()
b.is_raise=True
_str=input("pls input the expression: ")
print(b.calc(_str))

class Account:
    def __init__(self, number):
        self.number = number
        self.balance = 0
    def deposit(self, amount):
        assert amount > 0
        self.balance += amount
    def withdraw(self, amount):
        assert amount > 0
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("balance is not enough.")
import sys

import copy
class MyCopy:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
foo = MyCopy(7)
a = ["foo", foo]
b=a[:]
c=list(a)
d = copy.copy(a)
e=copy.deepcopy(a)
a.append("abc")
foo.value = 17
if __name__ == "__main__":
    print("Original: %r\n slice: %r\n list(): %r\n copy(): %r\n deepcopy(): %r\n" %(a,b,c,d,e))
'''
import os
os.rename("first.txt", "new.txt")