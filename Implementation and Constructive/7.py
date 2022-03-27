
def pattern(p,n):
    if p==1:
        return "#"*n
    elif p==2:
        return "."*(n-1)+"#"
    elif p==3:
        return "#"*n
    elif p==4:
        return "#"+"."*(n-1)
    
inp=list(map(int,input().split()))
p=1
for i in range(inp[0]):
    if p==5:
        p=1
    print(pattern(p,inp[1]))
    p+=1


