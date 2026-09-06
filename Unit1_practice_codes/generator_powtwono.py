def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2**n
        n += 1
a = PowTwoGen(2)
for n in a:
    print(n)
