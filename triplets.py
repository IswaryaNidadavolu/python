x = [0, -1, 2, -3, 1]
n=len(x)
found=True
for i in range(0,n-2):
    for j in range(i+1,n+1):
        for k in range(j+1,n):
            if (x[i] + x[j] + x[k]==0):
                print(x[i],x[j],x[k])
                found=True
if(found==False):
        print("not found")

