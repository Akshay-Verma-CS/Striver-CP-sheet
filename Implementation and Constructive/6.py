def solve(n):
    result=[];power=0
    while n!=0:
        digit=n%10
        # print("number = ",n)
        # print("digit = ",digit)
        # print("power = ",power)
        if digit==0:
            power+=1
        else:
            result.append(digit*pow(10,power))
            power+=1
        # print("result = ",result)
        n=n//10
    return result
t=int(input())
for i in range(t):
    query=int(input())
    ans=solve(query)
    print(len(ans))
    print(" ".join(list(map(str,ans))))   