t=int(input())
for i in range(t):
    x,a,b=map(int,input().split())
    z=(a*1)+(b*2)
    if z>=x:
        print("Qualify")
    else:
        print("NotQualify")