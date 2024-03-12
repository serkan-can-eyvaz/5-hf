def f(x,y):
    return x*y*(x+1)


def double_integral(a, b, c, d, n, m):
    h = (b-a)/n
    k = (d-c)/m
    toplam= 0
    for i in range(n):
        for j in range(m):
            xi = a + i*h
            xj = xi + h
            yi = c + j*k
            yj = yi + k
            toplam +=(h*k/4)*(f(xi, yi) + f(xi, yj) + f(xj, yi) + f(xj, yj))
    return toplam

result=double_integral(1,2,1,3,3,2)
print(result)