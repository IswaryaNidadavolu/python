n=int(input("enter the number"))
result=0
while n>0:
     div=n%10
     result=result+div
     n=n//10
print(result)
