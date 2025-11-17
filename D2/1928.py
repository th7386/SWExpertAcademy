from base64 import b64decode

T = int(input())

for tc in range(1, T + 1):
    word = input()
    res = b64decode(word).decode('UTF-8')

    print('#{} {}'.format(tc, res))
