N = int(input())
result = 0

for _ in range(N):
    word = input()
    while True:
        word = word.replace('AA', '')
        word = word.replace('BB', '')
        if 'AA' not in word and 'BB' not in word:
            break 
    if word == '':
        result += 1

print(result)