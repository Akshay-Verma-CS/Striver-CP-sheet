
def solve(Limak,Bob):
    year=0
    while Limak<=Bob:
        Limak*=3
        Bob*=2
        year+=1
    return year

x = list(map(int,input().split()))
print(solve(x[0],x[1]))