t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    k=(a+b)/2
    if k>c:
        print("YES")
    else:
        print("NO")