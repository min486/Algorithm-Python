T = int(input())

for tc in range(1, T+1):
    S = input()
    dic = {}

    for i in S:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    if len(dic) != 2:
        result = 'No'
    else:
        for j in dic.values():
            if j != 2:
                result = 'No'
                break
            else:
                result = 'Yes'

    print(f'#{tc} {result}')