T = 'abcdef'
dic = {}
for i, j in enumerate(T):
    dic[j] = i
    print("%s: %d" % (j, i))
