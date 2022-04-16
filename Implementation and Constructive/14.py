# 	977A - Wrong Subtraction
def solve(n,k):
    for i in range(k):
        if n%10!=0:
            n-=1
        else:
            n//=10
    return n
x = list(map(int,input().split()))
print(solve(x[0],x[1]))
    