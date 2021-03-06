# standard_library.py
"""Python Essentials: The Standard Library.
<Ehman Tannenholz>
<MTH 420>
<4/12/22>
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    return min(L), max(L), sum(L)/len(L)


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    
    int_1 = 1
    int_2 = int_1
    int_2 = 2
    int_2 == int_1
    #int is immutable

    str_1 = 'apples'
    str_2 = str_1
    str_2 = 'bananas'
    str_2 == str_1
    #str is immutable

    list_1 = [1,2,3]
    list_2 = list_1
    list_2[1] = 4
    list_2 == list_1
    #list is mutable

    tuple_1 = (1,2,3)
    tuple_2 = tuple_1
    tuple_2 += (1,)
    tuple_2 == tuple_1
    #tuple is immutable

    set_1 = {1,2,3}
    set_2 = set_1
    set_2.remove(1)
    set_2 == set_1
    #set is mutable

    print("int, string, and tuple are immutable.","list and set are mutable")
    
# Problem 3

def hypot(a,b):

    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt that are 
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    import calc
    import math
    return math.sqrt(calc.add(calc.pro(a,a),calc.pro(b,b)))


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    import itertools
    
    r = len(list(range(len(A))))
    powers=[]
    i = 0
    while i <= r:
        combo = itertools.combinations(A, i)
        powers.append(set(itertools.chain(combo)))
        i = i + 1
    return powers
