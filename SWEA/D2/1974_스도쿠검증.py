T = int(input())
 
def isPuzzle(matrix):
    # 가로 세로 검사
    for i in range(9):
        row_num = [0] * 10
        col_num = [0] * 10
        for j in range(9):
            row = matrix[i][j]
            col = matrix[j][i]

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
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        num = matrix[m][n]

                        if square[num]: 
                            return 0
                        square[num] = 1
    return 1
    
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, isPuzzle(puzzle)))