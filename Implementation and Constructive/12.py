def checkLucky(n):
    if count==0:
        return False
    while n!=0:
        if n%10==7 or n%10==4:
            n=n//10
        else:
            return False
    return True

if __name__=="__main__":
    n=int(input())
    count=0
    while(n!=0):
        if n%10==7 or n%10==4:
            count+=1
        n=n//10
    if checkLucky(count):
        print("YES")
    else:
        print("NO")