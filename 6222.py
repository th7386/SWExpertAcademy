words = input()

if words.isupper():
    print("%c(ASCII: %d) ==> %c(ASCII: %d)" % (words, ord(words), words.lower(), ord(words.lower())))
elif words.islower():
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(words, ord(words), words.upper(), ord(words.upper())))