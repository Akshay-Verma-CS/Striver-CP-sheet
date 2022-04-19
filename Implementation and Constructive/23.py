# 492A - Vanya and Cubes 
n =int(input())
c=0;j=0;t=0
while t<n:
    j+=1
    c = c + j
    t = t + c
    if t>n:
        j-=1
print(j)
