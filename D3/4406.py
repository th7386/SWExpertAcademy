T = int(input())
vowels = ["a", "e", "i", "o", "u"]
for tc in range(1, T + 1):
    data = input()
    result = ""
    for i in range(len(data)):
        if data[i] in vowels:
            continue
        result += data[i]
    print("#{} {}".format(tc, result))
