def list(n):
    for i in n:
        output=''
        times=i
        while(times>0):
            output = output + '*'
            times=times-1
        print(output) 

list([1,2,3,4])  
