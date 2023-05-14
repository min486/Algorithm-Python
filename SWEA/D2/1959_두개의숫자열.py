t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    n_li = list(map(int, input().split()))
    m_li = list(map(int, input().split()))
    max_value = 0
    
    # 두 숫자열의 길이 같을 때
    if n == m:
        for i in range(n):
            max_value += n_li[i] * m_li[i]
    else:
        if n > m:
            for i in range(n-m+1):
                result = 0
                for j in range(m):
                    result += n_li[i+j] * m_li[j]
                if result > max_value:
                    max_value = result
        else:
            for i in range(m-n+1):
                result = 0
                for j in range(n):
                    result += n_li[j] * m_li[i+j]
                if result > max_value:
                    max_value = result
                    
    print(f'#{tc} {max_value}')