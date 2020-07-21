def fun(n):
    return ((abs(1000-n)<=100) or (abs(2000-n)<=100))
print(fun(1000))
print(fun(900))
print(fun(800))
print(fun(2200))
