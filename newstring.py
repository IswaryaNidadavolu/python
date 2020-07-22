str=input("enter the string")
n=int(input("enter the copies"))
if len(str)<=2:
    print(str*n)
else:
    new=str[0:2]
    print(new*n)
