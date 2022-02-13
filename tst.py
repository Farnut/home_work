total = 0
for n in range(9990, 9999, 1):
    s = str(n)
    if s[0] != s[1] or s[0] != s[2] or s[0] != s[3] or s[1] != s[2] or s[1] != s[3] or s[2] != s[3]:
        total = total + 1
print(total)















