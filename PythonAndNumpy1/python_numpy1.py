# python_intro.py

"""Python Essentials: Introduction to Python.
Ehman Tannenholz
MTH 420
4-1-22
"""
print("Hello, world!")



if __name__ == "__main__":
    pass 




#Problem 1

pi = 3.14159
frac = 4/3
r=10
print(pi*frac*r**3)



#Problem 2

print("Hello, World!")



#Problem 3

def sphere_volume(r):
    """returns volume of sphere with radius r"""
    return 4/3*3.14159*r**3

print(sphere_volume(10))



#Problem 4

import numpy as np

A = np.array( [[3, -1, 4],[1, 5, -9]] )
B = np.array( [[2, 6, -5, 3],[5, -8, 9, 7],[9, -3, -2, -3]] )

def prob4(A,B):
    return A@B

print(prob4(A,B))



#Problem 5

def tax_liability(income):
    """Returns tax bracket from income"""
    if income < 9875:
        print("10%")
    elif income >= 9875.01 and income < 40125:
        print("12%")
    elif income >= 40125.01:
        print("22%")

tax_liability(10000)



#Problem 6

A = [1, 2, 3, 4, 5, 6, 7]
B = [5, 5, 5, 5, 5, 5, 5]
AB = []
AplusB = []
A5 = []

def prob6a(A,B):
    
    for num1,num2 in zip(A,B):
        AB.append(num1*num2)

    for num1,num2 in zip(A,B):
        AplusB.append(num1+num2)
    
    for num in A:
        A5.append(num1*5)

    return print(A5), print(AplusB), print (AB)
                  

prob6a(A,B)

import numpy as np

A = np.array([1, 2, 3, 4, 5, 6, 7])
B = np.array([5, 5, 5, 5, 5, 5, 5])

def prob6b(A,B):
    return print(A*B), print(A+B), print(A*5)

prob6b(A,B)
