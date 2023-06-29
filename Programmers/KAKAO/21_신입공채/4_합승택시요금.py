INF = int(1e9)

def floyd(arr, n):
    for k in range(1, n+1):  # 합승 지점
        for i in range(1, n+1):  # 출발 지점
            for j in range(1, n+1):  # 도착 지점
                if arr[i][k] + arr[k][j] < arr[i][j]:  # 최소 구간 갱신
                    arr[i][j] = arr[i][k] + arr[k][j]

def solution(n, s, a, b, fares):
    arr = [[INF for _ in range(n+1)] for _ in range(n+1)]  # 1~n 사용
    for i in range(1, n+1):
        arr[i][i] = 0

    for fare in fares:
        arr[fare[0]][fare[1]] = fare[2]
        arr[fare[1]][fare[0]] = fare[2]

    floyd(arr, n)

    answer = INF
    for k in range(1, n+1):
        # (합승 구간) + (a 가는 구간) + (b 가는 구간)
        answer = min(answer, arr[s][k] + arr[k][a] + arr[k][b])  # 최저 요금 갱신

    return answer