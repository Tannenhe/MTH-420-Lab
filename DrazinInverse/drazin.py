# drazin.py
"""Volume 1: The Drazin Inverse.
<Ehman Tannenholz>
<MTH 420>
<5-13-22>
"""

import numpy as np
from scipy import linalg as la


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k


# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    
    if np.allclose(np.matmul(A,Ad), np.matmul(Ad,A)):
        pass
    else:
        return False
    
    if np.allclose(np.matmul(np.linalg.matrix_power(A,k+1),Ad), np.linalg.matrix_power(A,k)):
        pass
    else:
        return False
    
    if np.allclose(np.matmul(Ad,np.matmul(A,Ad)), Ad):
        pass
    else:
        return False
    
    return True


# Problem 2
def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    T,Q = la.schur(A)
    f = lambda x: abs(x) > 0
    T1,Q1,k = la.schur(A, sort=f)
    g = lambda x: abs(x) <= 0
    T2,Q2,k2 = la.schur(A, sort=g)
    S = Q1[:,0:k]
    S = np.hstack((S,Q2[:,0:-k]))
    Sinv = np.linalg.inv(S)
    V = np.matmul(Sinv,np.matmul(A,S))
    Z = np.zeros(A.shape)
    Minv = np.linalg.inv(V[0:k,0:k])
    Z[:k,:k] = Minv
    
    return np.matmul(S,np.matmul(Z,Sinv))
    
    
def laplacian(A):
    """Compute the Laplacian matrix of the adjacency matrix A,
    as well as the second smallest eigenvalue.

    Parameters:
        A ((n,n) ndarray) adjacency matrix for an undirected weighted graph.

    Returns:
        L ((n,n) ndarray): the Laplacian matrix of A
    """
    D = A.sum(axis=1)    # The degree of each vertex (either axis).
    return np.diag(D) - A


# Problem 3
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    
    n = len(A)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i,j] = 0
            else:
                Lj = laplacian(A)
                Lj[j,:] = np.identity(n)[j,:]
                Ljd = drazin_inverse(Lj)
                A[i,j] = Ljd[i,i]
    return A
            
    
    
    


'''# Problems 4 and 5
class LinkPredictor:
    """Predict links between nodes of a network."""

    def __init__(self, filename='social_network.csv'):
        """Create the effective resistance matrix by constructing
        an adjacency matrix.

        Parameters:
            filename (str): The name of a file containing graph data.
        """
        raise NotImplementedError("Problem 4 Incomplete")


    def predict_link(self, node=None):
        """Predict the next link, either for the whole graph or for a
        particular node.

        Parameters:
            node (str): The name of a node in the network.

        Returns:
            node1, node2 (str): The names of the next nodes to be linked.
                Returned if node is None.
            node1 (str): The name of the next node to be linked to 'node'.
                Returned if node is not None.

        Raises:
            ValueError: If node is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete"


    def add_link(self, node1, node2):
        """Add a link to the graph between node 1 and node 2 by updating the
        adjacency matrix and the effective resistance matrix.

        Parameters:
            node1 (str): The name of a node in the network.
            node2 (str): The name of a node in the network.

        Raises:
            ValueError: If either node1 or node2 is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")'''
