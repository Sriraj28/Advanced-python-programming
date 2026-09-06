def func(max):
    count=1
    while count <= max :
        yield count
        count += 1

a = func(50)
for n in a:
    print(n)
