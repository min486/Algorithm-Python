T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end = ' ')
    word = input()
    
    if word == word[::-1]:
        print(1)
    else:
        print(0)