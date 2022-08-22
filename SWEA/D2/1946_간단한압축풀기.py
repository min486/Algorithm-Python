T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    
    li = []
    for i in range(N):
        alpha, num = input().split()
        for j in range(int(num)):
            li.append(alpha)
            
    cnt = 0
    for j in range(len(li)):
        print(li[j], end = '')
        cnt += 1
        if(cnt == 10):
            cnt = 0
            print()
    print()