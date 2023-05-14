t = int(input())

for tc in range(1, t+1):
    n = int(input())
    li = []
    print(f'#{tc}')
    
    for i in range(n):
        alpha, num = input().split()
        for j in range(int(num)):
            li.append(alpha)

    cnt = 0
    for j in range(len(li)):
        print(li[j], end='')
        cnt += 1
        
        if cnt == 10:
            cnt = 0
            print()
    print()