T = input().strip()
a = 0
b = 0
for i in T:
    if i.islower():
        a += 1

    elif i.isupper():
        b += 1

print("UPPER CASE %d" % b)
print("LOWER CASE %d" % a)
