# 	702A - Maximum Increase
n = int(input())
arr = list(map(int,input().split()))
maxx = 1
currentMaxx=1
for i in range(1,n):
    if arr[i]>arr[i-1]:
        currentMaxx+=1
    else:
        maxx = max(currentMaxx,maxx)
        currentMaxx=1
maxx = max(currentMaxx,maxx)
print(maxx)

