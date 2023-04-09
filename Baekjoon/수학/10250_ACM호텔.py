t = int(input())

for _ in range(t):
    # h개의 층, w개의 방, n번째 손님
    h, w, n = map(int, input().split())
    result = 0

    # 맨 왼쪽부터 아래에서 위로 배정
    if n % h != 0:
        # 방번호 = 층 * 100 + 호수
        result = (n % h) * 100 + (n // h) + 1
        
    # n번째 손님이 가장 높은 층에 있을 때
    else:
        result = h * 100 + (n // h)

    print(result)