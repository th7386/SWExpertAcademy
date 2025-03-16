def reverse(s):
    return s[::-1]

s = input()
if s == reverse(s):
    print(s)
    print("입력하신 단어는 회문(Palindrome)입니다.")