def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        x_nminus2 = 1
        x_nminus1 = 2
        x_n = x_nminus1 + x_nminus2
        for i in range(n-3):
            x_nminus2 = x_nminus1
            x_nminus1 = x_n
            x_n = x_nminus1 + x_nminus2
        return x_n

fib(10)

def fib_even(threshold):
    n = 0
    while fib(n) <= threshold:
        n += 1
    even_terms = 0
    for i in range(0,n):
        if fib(i) % 2 == 0:
            even_terms += fib(i)
    
    return even_terms

fib_even(4000000)

sum = 2
a,b = 1,2