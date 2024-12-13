N = Integer(int(input("N = "), 0))
e = Integer(int(input("e = "), 0))
d = Integer(int(input("d = "), 0))

k = d * e - 1
while True:
    g = randrange(2, N)
    print(f"Trying g = {g}")
    t = k
    found = False
    while True:
        if t % 2 != 0:
            break
        t //= 2
        x = Integer(pow(g, t, N))
        if x > 1 and (y := gcd(x - 1, N)) > 1:
            p = y
            assert N % y == 0
            q = N // y
            print(f"p = {p}")
            print(f"q = {q}")
            found = True
    if found:
        break


# This script attempts to factorize N by exploiting the relationship between d and e. It calculates k = d * e - 1 and randomly selects a g. For each g, it computes powers of g mod N and checks if the GCD of g^t - 1 and N is greater than 1, revealing factors of N if found. The process is based on Pollard's p-1 method.