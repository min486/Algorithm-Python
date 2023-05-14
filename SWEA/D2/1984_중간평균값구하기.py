t = int(input())

for tc in range(1, t+1):
    li = list(map(int, input().split()))
    li.sort()
    li.pop(0)
    li.pop(-1)
    
    result = round(sum(li) / len(li))
    print(f'#{tc} {result}')