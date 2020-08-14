list=[10,20,30,40]
n=len(list)
for i in range(0,n-1):
    for j in range(i+1,n):
        if (list[i]+list[j]==50):
            print(list[i],list[j])