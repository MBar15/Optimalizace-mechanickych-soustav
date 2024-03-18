def swann(f,x0,step):
    print(f(x0 - step) , f(x0) , f(x0 + step))
    if f(x0 - step) > f(x0) < f(x0 + step):
        return x0, [x0-step,x0+step]
    elif f(x0) < f(x0 + step):
        step = -step

    x_prev = x0
    k = 0
    while True:
        x_next = x_prev + 2**k * step

        if abs(f(x_next)) > abs(f(x_prev)):
            print(f(x_next),f(x_prev))
            break

        x_prev = x_next
        k += 1
    return x_prev, [x_prev- 2**(k-1) *step,x_prev+2**k*step]


def three_point_interval(f,a,b,epsilon):
    xm = 1/2*(a+b)
    L = b-a
    n = 0
    while  L>epsilon:
        x1 = a + L/4
        x2 = b - L/4
        
        if f(x1)<f(xm):
            b = xm
            xm = x1
        elif f(x2)<(xm):
            a = xm
            xm = x2
        else:
            a = x1
            b = x2 
        n = n+1
        L = b-a
    return a,b

def golden_search(f,a,b,epsilon):
    r = 0.618
    d = b-a
    n = 0
    while b-a>epsilon:
        d = d*r
        x1 = b-d
        x2 = a+d
        if f(x1)<=f(x2):
            b = x2
        else: a = x1
        n = n+1
    return a,b

def f(x):
    return (100-x)**2


def swanF(x):
    return (100 - x)**2

if __name__ == '__main__':

    #a,b = three_point_interval(f,60,150,0.001)
    #print('3_point search a,b:', a,b)
    #a,b = golden_search(f,60,150,0.001)
    #print('Golden search a,b:', a,b)

    #print('Val of minimum:',f((b+a)/2))


    print(swann(swanF,30,5))
