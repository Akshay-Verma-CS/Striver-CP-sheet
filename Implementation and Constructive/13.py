# 116A - Tram
n = int(input())
maxx=0
current_cap = 0
for i in range(n):
    x = list(map(int,input().split()))
    current_cap=(current_cap - x[0]) + x[1]
    maxx=max(current_cap,maxx)
print(maxx)
    