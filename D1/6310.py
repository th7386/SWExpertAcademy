import random

char_set = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
length = 8
passwd_list = random.choices(char_set, k=length)
passwd = "".join(passwd_list)
print(passwd)
