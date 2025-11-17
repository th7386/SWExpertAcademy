letters = input()
alpha = dict()
for i in letters:
    alpha[i] = alpha.get(i, 0) + 1
for key, value in alpha.items():
    print("{},{}".format(key, value))
