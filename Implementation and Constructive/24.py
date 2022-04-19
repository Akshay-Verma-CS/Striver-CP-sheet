# 1433A - Boring Apartments
t  = int(input())
d = { 1:1, 2:3, 3:6, 4:10}
for i in range(t):
    n = int(input())
    digit = n%10
    nlen = len(str(n))
    ans = d[nlen]
    while digit!=1:
        ans+=10
        digit-=1
    print(ans)

