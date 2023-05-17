t = 10

for tc in range(1, t+1):
    n = int(input())
    arr = [input() for _ in range(8)]
    result = 0

    for rc in range(8):
        for s in range(8-n+1):
            e = s + n - 1
            for i in range(n//2):
                if arr[rc][s+i] != arr[rc][e-i]: 
                    break
            else:
                result += 1
        
            for i in range(n//2):
                if arr[s+i][rc] != arr[e-i][rc]: 
                    break
            else:
                result += 1

    print(f'#{tc} {result}')