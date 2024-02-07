import math

t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=math.ceil(n/6)
    print(a*x)