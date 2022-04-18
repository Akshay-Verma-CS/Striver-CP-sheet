s = input()
initial = ord(s[0])
print(s if initial<97 else (chr(initial-32)+s[1:]))