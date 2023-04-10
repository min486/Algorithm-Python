a_cards = list(map(int, input().split()))
b_cards = list(map(int, input().split()))

# 두 리스트의 숫자들이 전부 같을 경우
if a_cards == b_cards:
    print(10, 10)
    print('D')
else:
    a = b = 0
    for i in range(10):
        if a_cards[i] > b_cards[i]:
            a += 3
            result = 'A'
        elif a_cards[i] < b_cards[i]:
            b += 3
            result = 'B'
        else:
            a += 1
            b += 1
    print(a, b)

    # 총 승점이 같을 경우
    if a == b:
        print(result)
    else:
        if a > b:
            print('A')
        elif a < b:
            print('B')