#1095A - Repeating Cipher 
n = int(input())
s = input()
i=0;j=0;res=""
while i<n:
    res+=s[i+j]
    j+=1
    i+=j
print(res)
