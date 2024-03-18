def f(x):
    return 2*x**2 + 16/x

def df(x):
    return 4*x - 16/x**2

def ddf(x):
    return 4 + 32/x**3


def newton_raphson(df,ddf,x0,epsilon):
    xk = x0
    while abs(df(xk)) > epsilon:
        xk = xk-df(xk)/ddf(xk)

    return xk


def bisection(df,a,b,epsilon):
    
    while b-a> epsilon:
        midpoint = (b+a)/2
        if df(midpoint)*df(a) > 0:
            a = midpoint
        else: b = midpoint

    return midpoint


def secant(df,a,b,epsilon):
    x2 = b
    x1 = a
    x = (b+a)/2
    while abs(df(x))>epsilon:
        x = x2 - df(x2)*(x2-x1)/(df(x2) - df(x1))
        x2 = x

    return x


if __name__ == '__main__':
    epsilon = 0.01

    x0 = 1
    xmin_NR = newton_raphson(df,ddf,x0,epsilon)
    print('Newton-Raphson:',xmin_NR)

    a = 1
    b = 5
    xmin_BI = bisection(df,a,b,epsilon)
    print('Bisection:',xmin_BI)

    a = 1
    b = 5
    xmin_SE = secant(df,a,b,epsilon)
    print('Secant:',xmin_SE)