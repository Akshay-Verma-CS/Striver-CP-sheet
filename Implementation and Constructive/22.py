# 1097A - Gennady and a Card Game
s=input()
rank = s[0]; suit = s[1]
arr = input().split()
flag=0
for i in arr:
    if i[0] == rank or i[1] == suit:
        flag=1
        break
print("YES" if flag==1 else "NO")