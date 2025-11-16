def function(list):
    a = len(list)
    maxvalue = list[0]
    for i in range(1, a):
        if list[i] > maxvalue:
            maxvalue = list[i]
    return maxvalue


list = [3, 5, 4, 1, 8, 10, 2]
print("max(3, 5, 4, 1, 8, 10, 2) => %d" % function(list))
