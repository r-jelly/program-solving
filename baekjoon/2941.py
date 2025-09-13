'''
Level: S2
Time: 16m39s
'''

word = input()

word = list(word)
cnt = 0
while word:
    char = word.pop()
    
    if char == "-":
        word.pop()
    elif char == "=":
        c = word.pop()
        if word:
            if c == 'z' and word[-1] == 'd':
                word.pop()
    elif char == "j":
        if word:
            if word[-1] == 'l' or word[-1] == 'n':
                word.pop()
    cnt += 1

print(cnt)