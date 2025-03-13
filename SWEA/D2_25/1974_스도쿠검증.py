def solve(arr):
    for i in range(9):
        row_li = [0] * 10
        col_li = [0] * 10
        for j in range(9):
            row = arr[i][j]
            col = arr[j][i]

            if row_li[row]:
                return 0
            if col_li[col]:
                return 0

            row_li[row] = 1
            col_li[col] = 1

            if i % 3 == 0 and j % 3 == 0:
                nemo = [0] * 10
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        num = arr[m][n]

                        if nemo[num]:
                            return 0
                        
                        nemo[num] = 1
    return 1

t = int(input())

for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = solve(arr)
    print(f'#{tc} {ans}')