# python_intro.py

"""Python Essentials: Introduction to Python.
Ehman Tannenholz
MTH 420
4-1-22
"""
print("Hello, world!")



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



#Problem 4


def prob4():
    import numpy as np
    A = np.array( [[3, -1, 4],[1, 5, -9]] )
    B = np.array( [[2, 6, -5, 3],[5, -8, 9, 7],[9, -3, -2, -3]] )
    return print(A@B)



#Problem 5

def tax_liability(income):
    """Returns tax bracket from income"""
    if income < 9875:
        return print("10%")
    elif income >= 9875.01 and income < 40125:
        return print("12%")
    elif income >= 40125.01:
        return print("22%")




#Problem 6



def prob6a():
    
    A = [1, 2, 3, 4, 5, 6, 7]
    B = [5, 5, 5, 5, 5, 5, 5]
    AB = []
    AplusB = []
    A5 = []
    
    for num1,num2 in zip(A,B):
        AB.append(num1*num2)

    for num1,num2 in zip(A,B):
        AplusB.append(num1+num2)
    
    for num in A:
        A5.append(num*5)

    return print(A5), print(AplusB), print (AB)
