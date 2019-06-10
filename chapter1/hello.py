#!/usr/bin/python
'''
a=input("Pls input a number: ")
if a>10:
    print("The number more than ten!")
elif a == 10:
    print("The number you are smart!")
else:
    print("The number less than 10!")
'''
quot = []

for n in range(1,100):
    if n %3 == 0:
        quot.append(n)
print(quot)
