def find(arr, leng):
    for rc in range(n):
        for s in range(n-leng+1):
            e = s + leng - 1
            for i in range(leng//2):
                if arr[rc][s+i] != arr[rc][e-i]:
                    break
            else:
                return True
            for i in range(leng//2):
                if arr[s+i][rc] != arr[e-i][rc]:
                    break
            else:
                return True
    return False

t = 10

for tc in range(1, t+1):
    _ = input()
    n = 100
    arr = [input() for _ in range(n)]

    for leng in range(n, 0, -1):
        if find(arr, leng):
            break

    print(f'#{tc} {leng}')