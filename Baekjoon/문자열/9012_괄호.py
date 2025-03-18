t = int(input())

for _ in range(t):
    text = input()
    cnt = 0

    for i in text:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
            if cnt < 0:
                print('NO')
                break
    else:
        if cnt == 0:
            print('YES')
        else:
            print('NO')