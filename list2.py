def fun(num):
    position=2
    index=0
    length=len(num)
    while(length>0):
      index=(position+index)%length
      print(num.pop(index))
      length-=1
  
x=[10,20,30,40,50,60,70,80,90]
fun(x)
