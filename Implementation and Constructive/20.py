# 1368A - C+=
def solve(a,b,x):
    count=0
    while a<=x and b<=x:
        if a>b:
            b+=a
            count+=1
        else:
            a+=b
            count+=1
    return count
t = int(input())
for i in range(t):
    x = list(map(int,input().split()))
    print(solve(x[0],x[1],x[2]))