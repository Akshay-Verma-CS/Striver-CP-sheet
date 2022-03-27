inp=list(map(int,input().split()))
x=inp[0];y=inp[1];z=inp[2]
xy=abs(x-y);xz=abs(x-z);yz=abs(y-z)
d1=xy+xz;d2=xy+yz;d3=xz+yz
print(min(d1,d2,d3))