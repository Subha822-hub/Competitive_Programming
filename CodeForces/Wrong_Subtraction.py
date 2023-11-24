x,y=map(int,input().split())
b=str(x)
for i in range(y):
    if( int(b[-1]) != 0):
        b=int(b)-1
        b=str(b)
    else:
        b=int(int(b)/10)  
        b=str(b)
print(int(b))