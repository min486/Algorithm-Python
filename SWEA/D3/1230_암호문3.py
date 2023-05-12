t = 10

for tc in range(1, t+1):
    n = int(input())
    result_li = input().split()
    m = int(input())
    order_li = input().split()
    i = 0

    for _ in range(m):
        ida = order_li[i]
        if ida == 'I':
            order = int(order_li[i+1]) 
            cnt = int(order_li[i + 2]) 
            for idx in range(cnt):
                result_li.insert(order+idx, order_li[i+3+idx])
            i += 3+cnt
        elif ida == 'D':
            order = int(order_li[i+1]) 
            cnt = int(order_li[i+2]) 
            for _ in range(cnt):
                result_li.pop(order)
            i += 3
        elif ida == 'A':
            cnt = int(order_li[i+1])
            for idx in range(cnt):
                result_li.append(order_li[i+2+idx])
            i += 2 + cnt

    print(f'#{tc}', *result_li[:10])