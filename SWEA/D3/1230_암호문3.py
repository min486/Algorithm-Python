t = 10

for tc in range(1, t+1):
    n = int(input())
    result_li = input().split()
    m = int(input())
    order_li = input().split()
    i = 0

    while i < len(order_li):
        if order_li[i] == 'I':
            order = int(order_li[i+1]) 
            if order < 10:
                for idx in range(order):
                    result_li.insert(order+idx, order_li[i+3+idx])
            i = i+3+order

        elif order_li[i] == 'D':

        elif order_li[i] == 'A':
