t = 10

for tc in range(1, t+1):
    n = int(input())
    result_li = input().split()
    m = int(input())
    order_li = input().split()
    i = 0

    while i < len(order_li):
        order = int(order_li[i+1])
        cnt = int(order_li[i+2])
        # 10개 숫자 필요하므로
        if order < 10:
            # 명령어들 순차적으로 삽입하기 위해 index 활용
            for idx in range(cnt):
                result_li.insert(order+idx, order_li[i+3+idx])
        i += 3+cnt  # 다음 명령어로 이동

    print(f'#{tc}', *result_li[:10])