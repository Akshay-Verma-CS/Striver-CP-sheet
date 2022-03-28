n=int(input())
arr=list(map(int,input().split()))
idx_max=0;idx_min=0
minn=arr[0];maxx=arr[0]
for i in range(n):
    if arr[i]<=minn:
        minn=arr[i]
        idx_min=i
    elif arr[i]>maxx:
        maxx=arr[i]
        idx_max=i
if idx_max>idx_min:
    print(idx_max+(n-1-idx_min-1))
else:
    print(idx_max+(n-1-idx_min))
