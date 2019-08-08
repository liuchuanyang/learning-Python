#!/usr/bin/python
'''
a=input("Pls input a number: ")
if a>10:
    print("The number more than ten!")
elif a == 10:
    print("The number you are smart!")
else:
    print("The number less than 10!")

quot = []

for n in range(1,100):
    if n %3 == 0:
        quot.append(n)
#print(quot)
name = {"name":"liu", "lang":"python","website":"github"}
for i,j in name.iteritems():
    print("{}--->{}".format(i, name[i]))
c=[]
for i in name:
    c.append(i+name[i])
print(c)
seasons=['Spring', 'Summer', 'Fall', 'Winter']
mylist=list(enumerate(seasons, start=1))
print(mylist)
raw = "Do you love liu? liu is a good man"
raw_list = raw.split(" ")
print(raw_list)
for i, string in enumerate(raw_list):
    if  'liu' in string:
        raw_list[i]='huan'
print(raw_list)
squares=[x**2 for x in range(1,10)]
#print(squares)

#print(raw.strip())
se= [' Spring ', ' Summer ', ' Fall ', ' Winter ']
print([one.strip() for one in se])
num_input=input("Pls input one integer that is in 1 to 100: ")

if int(num_input) < 0 or int(num_input) >= 100:
    print("The number should be in 1 to 100.")
else:
    print("Hello")
'''
def readFile(filename):
    f = open(filename)
    for line in f:
        print(line)
    f.close()
#nf = open("file.txt", "w")
#nf.write("This is a file")
#nf.close()
#readFile("file.txt")
'''
with open("test.txt", "a") as f:
    f.write("\n This is about 'with...as...")
readFile("test.txt")
'''
'''
import os
import time
file_stat=os.stat("test.txt")
print(time.localtime(file_stat.st_ctime))
f = open("file.txt")
'''
'''
content=f.read()
print(content)
f.close()

while True:
    s=f.readline()
    if s == "":
        break
    print(s)
else:
    pass

content = f.readlines()
print(content)

import fileinput 
for line in fileinput.input("file.txt"):
    print(line)
'''

#print(lst)

#iter_list=iter(lst)

'''
def func(x, *arg):
    print(x)
    result = x
    print(arg)
    for i in arg:
        result += i
    return result
print(func(1,2,3,4,5,6,7,8,9))
'''

def book(author, name):
    print("{0} is writing {1}".format(author, name))

bars={"name":"Starter learning Python", "author":"Kivi"}
def foo(p1, p2, p3):
    """hello world"""
    print("p1----->{}".format(p1))
    print("p2----->{}".format(p2))
    print("p3----->{}".format(p3))
'''
lam = lambda x: x+3
n2=[]
for i in range(10):
    n2.append(lam(i))
print(n2)
g=lambda x:x**2
print(g(3))
lamb = [lambda x:x, lambda x:x**2, lambda x:x**3, lambda x:x**4]
for i in lamb:
    print("{}".format(i(2)))
print("hello world")
print(lambda x:x+3, range(10))
'''
lst1=[1,2,3,4,5]
lst2=[6,7,8,9,0]
lst3=[7,8,9,2.1]

#lst4=map(lambda x, y,z:x+y+z, lst1,lst2,lst3)
#print(lst4)

import math
def quadratic_equation(a,b,c):
    delta=b*b-4*a*c
    if delta < 0:
        return False
    elif delta == 0:
        return -(b/(2*a))
    else:
        sqrt_delta=math.sqrt(delta)
        x1 = (-b + sqrt_delta)/(2*a)
        x2 = (-b - sqrt_delta)/(2*a)
        return x1,x2
if __name__ == "__main__":
    print("A quadratic_equation: x^2 +2*x + 1 = 0")
    cofficient = (1,2,1)
    roots=quadratic_equation(*cofficient)
    if roots:
        print("The result is:%",roots)
    else:
        print("This equation has no solution")




