score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0

while (len(score) > 0):
    i = score.pop()
    if i >= 80:
        sum += i
print(sum)
