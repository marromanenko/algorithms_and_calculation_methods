import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.ticker as ticker
import pylab
from math import fabs
from prettytable import PrettyTable

def f1(x):
    return np.cosh(x)*np.sin((np.e)**x)-5*((np.e)**x)*np.cos(x)

def f2(x):
    return 5*(np.e**x)*np.sin(x)+(np.e**x)*np.cos(np.e**x)*np.cosh(x)-5*(np.e**x)*np.cos(x)+np.sin(np.e**x)*np.sinh(x)

def f3(x):
    return -np.e**(2*x)*np.sin(np.e**x)*np.cosh(x)+10*(np.e**x)*np.sin(x)+2*np.e**x*np.cos(np.e**x)*np.sinh(x)+np.e**x*np.cos(np.e**x)*np.cosh(x)+np.sin(np.e**x)*np.cosh(x)
 
def fur(x, f1, f3):
    return f1(x)*f3(x)>0

def mon(a, b, f2):
    return f2(a)*f2(b)>0

def zero_check(a, b, f1):
    return f1(a)*f1(b)<0

def f(x):
    return x*np.sin((np.e)**x)+0.5*x
    
def sgn(x):
    if (x>0):
        return 1
    elif (x<0):
        return -1
    else:
        return 0
 
def root(a,b,epsX,epsF):
    tab = PrettyTable()
    it=0
    tab.field_names = ["iteration", "a", "b", "x"]
    if sgn(f(a))*sgn(f(b))>0:  
        return None        
    while(True):
        c=0.5*(a+b)
        x=c
        if (fabs(b-a)<=epsX) or (f(x)==0):
            tab.add_row([it, a, b, x]) 
            print(tab)
            return c
        elif sgn(f(a))*sgn(f(c))<0:
            b=c
        else:
            a=c
        tab.add_row([it, a, b, x])
        it+=1

def function43(x):
    return (np.sqrt(5-x))*np.sin(x)+ x*np.cos(math.pi-x)

def function43_derivative1(x):
    return (-np.sin(x)/(2*np.sqrt(5-x)))+(np.sqrt(5-x))*np.cos(x)-np.cos(x)+x*np.sin(x)

def function43_derivative2(x):
    return ((-2 * (5 - x) * np.cos(x) + np.sin(x)) / ((np.sqrt(5 - x)) * (20 - 4 * x))) - ((np.cos(x)) / (2 * np.sqrt(5 - x))) - (np.sqrt(5 - x)) * np.sin(x) + np.sin(x) + np.cos(x) - x * np.sin(x)

def stef(f1, f2, f3, a, b):
    tab = PrettyTable()
    tab.field_names = ["method", "iteration", "x"]
    maxiter = 100
    eps = 0.0000001
    k=0
    if fur(a, f1, f3) == True:
        x=a
    else:
        x=b
    while np.abs(f1(x) - eps) > 0.01:
        x1=x
        x = x - f1(x) / f2(x);
        tab.add_row(["Newton", k, x1])
        k=k+1
    while True:
        x1=x
        x=x-(f1(x)*f1(x))/(f1(x+f1(x))-f1(x))
        tab.add_row(["Stef", k, x])
        if(k>=maxiter or np.abs(x-x1)<=eps):
            break
        k=k+1
    print(tab)
    return x

if __name__=='__main__':
    print("method of division in half")

    a=-0.5
    b=0.5
    r=root(a,b,1e-8,1e-14)
    print("root = ", r)

    a=1.0
    b=1.4
    r=root(a,b,1e-8,1e-14)
    print("root = ", r)

    a=1.6
    b=2.0
    r=root(a,b,1e-8,1e-14)
    print("root = ", r)

    a=2.0
    b=2.4
    r=root(a,b,1e-8,1e-14)
    print("root = ", r)

    a=2.4
    b=2.6
    r=root(a,b,1e-8,1e-14)
    print("root = ", r)

    a=2.6
    b=2.8
    r=root(a,b,1e-8,1e-14)
    print("root = ", r)

    a=2.8
    b=3.0
    r=root(a,b,1e-8,1e-14)
    print("root = ", r)

    print("Steffenson's method")

    a=4.645
    b=4.65
    if zero_check(a,b,f1) and mon(a,b,f2):
        r=stef(f1,f2, f3,a,b)
    print("root = ", r)

    a=4.66
    b=4.67
    if zero_check(a,b,f1) and mon(a,b,f2):
        r=stef(f1,f2, f3,a,b)
    print("root = ", r)

    a=4.70035
    b=4.71
    if zero_check(a,b,f1) and mon(a,b,f2):
        r=stef(f1,f2, f3,a,b)
    print("root = ", r)

    a=4.7285
    b=4.73
    if zero_check(a,b,f1) and mon(a,b,f2):
        r=stef(f1,f2, f3,a,b)
    print("root = ", r)

    a=4.752
    b=4.76
    if zero_check(a,b,f1) and mon(a,b,f2):
        r=stef(f1,f2, f3,a,b)
    print("root = ", r)

    a=4.7825
    b=4.79
    if zero_check(a,b,f1) and mon(a,b,f2):
        r=stef(f1,f2, f3,a,b)
    print("root = ", r)

    a=4.795
    b=4.8
    if zero_check(a,b,f1) and mon(a,b,f2):
        r=stef(f1,f2, f3,a,b)
    print("root = ", r)

    x = np.linspace(4, 5, 200)
    #x = np.linspace(-5, 3, 200)

    y = np.cosh(x)*np.sin(np.e**x) - 5*np.e**x * np.cos(x)
    #y = x*np.sin((np.e)**x)+0.5*x

    fig, ax = plt.subplots()

    ax.plot(x, y, color = 'r', linewidth = 1)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
    #ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

    ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))

    ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
    #ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

    ax.grid(which='major',
            color = 'k')

    ax.minorticks_on()
    ax.grid(which='minor',
            color = 'gray',
            linestyle = ':')

    fig.set_figwidth(12)
    fig.set_figheight(8)

    plt.show()
