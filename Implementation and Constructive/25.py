#  	1303A - Erasing Zeroes
from itertools import count


t =int(input())
for i in range(t):
    n = str(input())
    r = len(n)-1;l=0;countl=0;countr=0
    f1 = f2 = False
    while l<=r:
        if n[l] == "1":
            f1=True
        if n[r]=="1":
            f2=True
        if f1 == True and n[l] == "0" and l!=r:
            countl+=1
        if f2==True and n[r]=="0":
            countr+=1
        l+=1
        r-=1
    print((countl+countr) if (f1&f2) else 0)
        
        






            