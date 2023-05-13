def solve(arr):
    for i in range(9):
        row_num = [0] * 10
        col_num = [0] * 10
        for j in range(9):
            row = arr[i][j]
            col = arr[j][i]

            # 중복 체크
            if row_num[row]:
                return 0
            if col_num[col]:
                return 0

            row_num[row] = 1
            col_num[col] = 1

            # 3x3 격자 검사
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for n in range(i, i+3):
                    for m in range(j, j+3):
                        num = arr[n][m]

                        if square[num]: 
                            return 0
                        square[num] = 1
    return 1

t = int(input())

for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = solve(arr)
    print(f'#{tc} {result}')