T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_value = 0
    
    # 두 숫자열의 길이가 같을 때는 자리끼리 곱하기
    if N == M:
        for i in range(N):
            max_value += A[i] * B[i]
    else:
        if N > M:
            for i in range(N-M+1):
                result = 0
                for j in range(M):
                    result += A[i+j] * B[j]
                if result > max_value:
                    max_value = result
        else:
            for i in range(M-N+1):
                result = 0
                for j in range(N):
                    result += B[i+j] * A[j]
                if result > max_value:
                    max_value = result
                    
    print(f'#{tc} {max_value}')