import math
def f(x):
    return math.e**x
def simpson(x0,xn,n):
    h=(xn-x0)/n
    S=f(x0)+f(xn)
    for i in  range(1,n):
        k=x0+i*h
        if i%2==0:
            S=S+2*f(k)
        else:
            S=S+4 *f(k)
    S=S*h/3
    return S
a=float(input("alt limit:"))
b=float(input("ust limit: "))
n=int(input("alt aralık:"))
sonuc=simpson(a,b,n)
print("deger: %0.6f"%(sonuc))

