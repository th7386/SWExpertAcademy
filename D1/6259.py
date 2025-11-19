lst = list(map(str, input()))
n_cnt, w_cnt = 0, 0

for i in lst:
    if i.isalpha():
        w_cnt += 1
    elif i.isdigit():
        n_cnt += 1

print(f'LETTERS {w_cnt} \nDIGITS {n_cnt}')
