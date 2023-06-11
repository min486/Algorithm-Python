def check_row():
    global result

    for k in range(n):
        leng = 1
        for l in range(n-1):
            if arr[k][l] == arr[k][l+1]:
                leng += 1
                result = max(result, leng)
            else:
                leng = 1

def check_col():
    global result

    for k in range(n):
        leng = 1
        for l in range(n-1):
            if arr[l][k] == arr[l+1][k]:
                leng += 1
                result = max(result, leng)
            else:
                leng = 1

n = int(input())
arr = [list(input()) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n-1):
        # 두 원소 다르면 (가로)
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]  # 두 값 교환
            check_row()  # 가로 확인
            check_col()  # 세로 확인
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]  # 원래대로
        # 두 원소가 다르면 (세로)
        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            check_row()
            check_col()
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]

print(result)