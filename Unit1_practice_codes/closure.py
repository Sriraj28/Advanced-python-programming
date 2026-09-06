def outer(x):   #accepts the x value and defines the inner function
    def inner(y):
        return x+y         #remebers the x value from the outer function even after the function is finished
    return inner            #return the inner function (closure)

a = outer(50)    #stores value of x in outer

print(a(50))      #accesses the value from outer and gives value to inner 
print(a(100))       #same as above
