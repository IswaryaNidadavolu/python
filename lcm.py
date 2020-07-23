def fun(n1,n2):
    if n1>n2:
        higher=n1
    else:
        higher=n2
    value=higher
    while True:
        if higher%n1==0 and higher%n2==0:
            print("lcm is",higher)
            break
        else:
            higher=higher+higher



n1=int(input("enter the number"))
n2=int(input("enter the number"))
fun(n1,n2)