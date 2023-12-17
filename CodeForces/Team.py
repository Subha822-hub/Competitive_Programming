n=int(input())
a=0
for i in range(n):
    x,y,z=map(int,input().split())
    sum=x+y+z
    sums=int(sum/2)
    if sums==1:
        a=a+sums
    else:
        pass
print(a)