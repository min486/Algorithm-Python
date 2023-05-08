alpha = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())

for tc in range(1, t+1):
    line = input()
    cnt = 0
    
    for i in range(len(line)):
        if line[i] == alpha[i]:
            cnt += 1
        else:
            break
            
    print(f'#{tc} {cnt}')