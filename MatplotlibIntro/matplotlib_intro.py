# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Ehman Tannenholz>
<MTH 420>
<4/29/22>
"""


# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    import numpy as np
    
    matrix = np.random.normal(size=(n,n))
    means = matrix.mean(axis=1)
    variance = matrix.var(axis=1)
    return print("Means:", means, "Variances:", variance)
    

def var_of_means2(n):
    """no printed output
    """
    import numpy as np
    
    matrix = np.random.normal(size=(n,n))
    means = matrix.mean(axis=1)
    variance = matrix.var(axis=1)
    return variance

def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    from matplotlib import pyplot as plt
    
    for i in [100,200,300,400,500,600,700,800,900,1000]:
        temp = plt.plot(var_of_means2(i))
        plt.show(temp)
        


# Problem 2

def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    from matplotlib import pyplot as plt
    import numpy as np
    
    x = np.linspace(-np.pi,np.pi,50)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.arctan(x)
    plt.plot(x,y1)
    plt.show()
    plt.plot(x,y2)
    plt.show()
    plt.plot(x,y3)
    plt.show()

# Problem 3
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    from matplotlib import pyplot as plt
    import numpy as np
    
    x1 = np.linspace(-2,0.99,50)
    x2 = np.linspace(1.01,6,50)
    y1 = 1/(x1-1)
    y2 = 1/(x2-1)
    A = plt.plot(x1,y1,'m--',linewidth = 4)
    B = plt.plot(x2,y2,'m--',linewidth = 4)
    plt.xlim(-2,6)
    plt.ylim(-6,6)
    plt.show(A,B)
    
    


# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    from matplotlib import pyplot as plt
    import numpy as np
    
    x = np.linspace(0,2*np.pi,50)
    
    plt.subplot(221)
    plt.plot(x, np.sin(x),'g-')
    plt.title('Sin(x)')
    plt.subplot(222)
    plt.plot(x, np.sin(2*x),'r--')
    plt.title('Sin(2x)')
    plt.subplot(223)
    plt.plot(x,2*np.sin(x),'b--')
    plt.title('2Sin(x)')
    plt.subplot(224)
    plt.plot(x,2*np.sin(2*x),'m:')
    plt.title('2Sin(2x)')
    plt.axis([0, 2*np.pi, -2, 2])
    plt.suptitle('Sin functions with constants')
    plt.show()
    
    


# Problem 5
def prob5():
    """Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    import numpy as np
    from matplotlib import pyplot as plt
    fars = np.load('FARS.npy')
    
    plt.subplot(121)
    plt.plot(fars[:,1],fars[:,2],'k,')
    plt.axis('equal')
    plt.xlabel('Longitude')
    plt.ylabel('Lattitude')
    plt.show
    plt.subplot(122)
    plt.hist(fars[:,0],bins = 24)
    plt.xlabel('24h Time')
    plt.xlim(0,24)
    plt.show
    


# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    import numpy as np
    from matplotlib import pyplot as plt
    
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = x.copy()
    X, Y = np.meshgrid(x, y)
    Z = (np.sin(X) * np.sin(Y))/(X*Y)
    
    plt.subplot(121)
    plt.pcolormesh(X, Y, Z, cmap="viridis")
    plt.colorbar()
    plt.xlim(-2*np.pi, 2*np.pi)
    plt.ylim(-2*np.pi, 2*np.pi)
    
    plt.subplot(122)
    plt.contour(X, Y, Z, 10, cmap="coolwarm")
    plt.colorbar()
    
    plt.show
