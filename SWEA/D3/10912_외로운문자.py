T = int(input())

for tc in range(1, T+1):
    string = input()
    li = []
    
    for ch in string:
        if ch not in li:
            li.append(ch)
        else:
            li.remove(ch)
    li.sort()
    
    if len(li) == 0:
        result = 'Good'
    else:
        result = ''.join(li)
    
    print(f'#{tc} {result}')