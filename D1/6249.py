T = int(input())
count_list = [0] * 10

while T > 0:
    count_list[T % 10] += 1  # T의 나머지 부분 즉 1의 자리를 찾아 카운트
    T = T // 10  # 몫을 구하여 반복

print(' '.join(map(str, [i for i in range(10)])))  # 리스트를 문자열로 만들어준다.
print(' '.join(map(str, count_list)))  # 마찬가지로 리스트를 문자열로 만들어준다.
