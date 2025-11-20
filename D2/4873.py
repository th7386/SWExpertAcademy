T = int(input())
for tc in range(1, T + 1):
    s = list(map(str, input()))
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    result = len(stack)
    print("#{} {}".format(tc, result))
