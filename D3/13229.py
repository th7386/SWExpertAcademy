T = int(input())
dic = {"MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4, "SAT": 5, "SUN": 6}
for tc in range(1, T + 1):
    S = input()
    result = dic["SUN"] - dic[S]
    if S == "SUN":
        result = 7
    print("#{} {}".format(tc, result))
