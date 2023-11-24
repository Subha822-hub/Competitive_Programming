t = int(input())
for i in range(t):
    w=input()
    first=w[0]
    last=w[-1]
    length=len(w)
    if(length>10):
       print(first+str(length-2)+last)
 
    else:
         print(w)