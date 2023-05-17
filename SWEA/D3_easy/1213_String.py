t = 10

for tc in range(1, t+1):
    _ = input()
    st = input()
    li = input()
    
    result = li.count(st)
    
    print(f'#{tc} {result}')