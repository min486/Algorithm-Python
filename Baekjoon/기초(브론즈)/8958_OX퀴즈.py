tc = int(input())

for _ in range(tc):
    string = input()
    result = 0
    cnt = 1

    for i in string:
        if i == 'O':
            result += cnt
            cnt += 1
        elif i == 'X':
            cnt = 1

    print(result)