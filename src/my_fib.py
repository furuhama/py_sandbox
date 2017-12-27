def my_fib(n):
    n1 = 1
    n2 = 1
    k = 1
    while k < n:
        n1, n2 = n2, n1 + n2
        k += 1

    return n1
