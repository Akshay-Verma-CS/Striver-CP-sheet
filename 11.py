n=int(input())
p=map(int,input().split())
d={}
for i,v in enumerate(p):
    d[v]=i+1
for i in range(n):
    print(d[i+1])