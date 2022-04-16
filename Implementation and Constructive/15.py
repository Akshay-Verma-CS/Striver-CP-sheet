# 	546A - Soldier and Bananas
def solve(cost,amount,noOfBanana):
    billAmount=0
    for i in range(noOfBanana):
        currentCost = cost * (i+1)
        billAmount+=currentCost
    if billAmount>amount:
        return billAmount-amount
    else:
        return 0

x = list(map(int,input().split()))
print(solve(x[0],x[1],x[2]))


