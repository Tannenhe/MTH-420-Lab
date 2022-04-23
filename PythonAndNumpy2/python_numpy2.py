# python_intro.py
"""Python Essentials: Introduction to Python.
<Ehman Tannenholz>
<MTH 420>
<4/22/22>
"""

#Problem 1
def isolate(a, b, c, d, e):
    
    return print(a,b,c,sep='     ',end=' '), print(d,e,sep=' ')




#Problem 2
def first_half(string):
    fhalf = int(0.5*len(string))
    return string[:fhalf]


def backward(first_string):
    back = ""
    for i in range(len(first_string)+1):
        back+=first_string[-i]
    return back






#Problem 3
def list_ops():
    list = ["bear","ant","cat","dog"]
    list.append("eagle")
    list[2] = "fox"
    list.pop(1)
    list.sort(reverse=True)
    list[list.index("eagle")] = "hawk"
    hunt = ["hunter"]
    list = list + hunt
    return list




#Problem 4
def alt_harmonic(n):
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximate ln(2).
    """
    harm = [(-1)**(i+1)/i for i in range(1,n+1)]
    return sum(harm)



def prob5(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    import numpy as np
    copy = A
    mask = A < 0
    copy[mask] = 0
    return copy

def prob6():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    import numpy as np
    A = np.arange(6).reshape(3,2)
    A = A.T
    B = np.zeros(9)
    maskB = [0,3,4,6,7,8]
    B[maskB]=3
    B = B.reshape((3,3))
    C = np.zeros(9)
    maskC = [0,4,8]
    C[maskC]=-2
    C = C.reshape((3,3))
    
    one = np.hstack((np.zeros((3,3)),A.T,np.eye(3)))
    two = np.hstack((A,np.zeros((2,2)),np.zeros((2,3))))
    three = np.hstack((B,np.zeros((3,2)),C))
    stack = np.vstack((one,two,three))
    
    return print(stack)

def prob7(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    


def prob8():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    raise NotImplementedError("Problem 8 Incomplete")

