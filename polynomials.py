def f(x):
    return 2*x**2 + 16/x



def quadratic_search(f,x1,x2,x3):
    f1 = f(x1) 
    f2 = f(x2) 
    f3 = f(x3) 

    a1 = (f2-f1)/(x2-x1)
    a2 = 1/(x3 - x2)*((f3 - f1)/(x3 - x1) - (f2 - f1)/(x2 - x1))

    x = (x2+x1)/2 - a1/(2*a2)

    return x

def successive_quadratic_search(f,x0,stepm,epsilon):
    x1 = x0
    x2 = x1+step
    if f(x2)>f(x1):
        x3 = x1-step
    else: x3 = x1+2*step

    while True:
        fn = [f(x1),f(x2),f(x3)]
        xn = [x1,x2,x3]
        Fmin = min(fn)
        Xmin = xn[fn.index(Fmin)]

        x = quadratic_search(f,x1,x2,x3)

        if abs(Fmin - f(x)) < epsilon or abs(Xmin - x) < epsilon: break

        xn.append(x)
        xn.sort()
        index = xn.index(x)
        x1 = xn[index-1]
        x2 = xn[index]
        x3 = xn[index+1]

    return x2


if __name__ == '__main__':
    x1 = 1
    x3 = 5
    x2 = (x3+x1)/2
    xMin = quadratic_search(f,x1,x2,x3)
    print('Quadratic search:',xMin)

    x0 = 1
    step = 1
    epsilon = 0.003
    xMin = successive_quadratic_search(f,x0,step,epsilon)
    print('Succesive quadratic search (powels method)',xMin)