# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name>
<Class>
<Date>
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
from matplotlib import pyplot as plt
import scipy
import scipy.linalg 

# Problem 1
def least_squares(a, B):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    
    A = scipy.array(a)
    b = scipy.array(B)
    QR = np.linalg.qr(A,mode='reduced')
    QTb = np.matmul(QR[0].T,b)
    return scipy.linalg.solve_triangular(QR[1],QTb)

'''scipy.linalg.solve(QR[1],QR[0].T*b)'''

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    housing = np.load("housing.npy")
    x = housing[:,0]
    y = housing[:,1]
    ones = np.ones((len(x),1))
    A = np.column_stack((x,ones))
    b = y
    lsq = least_squares(A, b)
    plt.scatter(x,y)
    plt.plot(x,lsq[0]*x+lsq[1])
    return(lsq)

# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    housing = np.load("housing.npy")
    x = housing[:,0]
    y = housing[:,1]
    xpoly = np.linspace(0,16,50)
    
    plt.subplot(221)
    plt.title('3rd order')
    three = np.vander(x,3)
    threeC = scipy.linalg.lstsq(three, y)[0]
    plt.plot(x,np.matmul(three,threeC))
    plt.scatter(x,y)
    
    plt.subplot(222)
    plt.title('6th order')
    six = np.vander(x,6)
    sixC = scipy.linalg.lstsq(six, y)[0]
    plt.plot(x,np.matmul(six,sixC))
    plt.scatter(x,y)
    
    plt.subplot(223)
    plt.title('9th order')
    nine = np.vander(x,9)
    nineC = scipy.linalg.lstsq(nine, y)[0]
    plt.plot(x,np.matmul(nine,nineC))
    plt.scatter(x,y)
    
    plt.subplot(224)
    plt.title('12th order')
    twelve = np.vander(x,12)
    twelveC = scipy.linalg.lstsq(twelve, y)[0]
    plt.plot(x,np.matmul(twelve,twelveC))
    plt.scatter(x,y)
    
    plt.show()
    


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
