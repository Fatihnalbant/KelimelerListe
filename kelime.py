s = input('Bir yazı giriniz:')

delims = ' \t.()!,-:?*[]%+;'

words = []
i = 0
while True:
    while i < len(s) and s[i] in delims:
        i += 1
    if i == len(s):
        break
    start = i

    while i < len(s) and s[i] not in delims:
        i += 1

    words.append(s[start:i])

print(words)
