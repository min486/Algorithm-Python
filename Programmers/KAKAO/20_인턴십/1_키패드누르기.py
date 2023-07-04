def near_hand(dic, l, r, num, hand):
    left_distance = abs(dic[l][0] - dic[num][0]) + abs(dic[l][1] - dic[num][1])  # 현재왼손과 누를번호의 x좌표, y좌표 계산
    right_distance = abs(dic[r][0] - dic[num][0]) + abs(dic[r][1] - dic[num][1])  # 오른손과의 거리

    if left_distance == right_distance:
        if hand == 'left':  # 왼손잡이면
            return 'L'
        else:
            return 'R'
    else:
        if left_distance < right_distance:  # 현재왼손과 가까우면
            return 'L'
        else:
            return 'R'

def solution(numbers, hand):
    left_li = [1, 4, 7]
    right_li = [3, 6, 9]
    now_li = ['*', '#']  # 현재 왼손, 오른손

    dic = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2),
    }

    answer = ''
    for num in numbers:
        if num in left_li:
            answer += 'L'
            now_li[0] = num
        elif num in right_li:
            answer += 'R'
            now_li[1] = num
        else:  # 2, 5, 8, 0
            nh = near_hand(dic, now_li[0], now_li[1], num, hand)  # 가까운 손 return
            if nh == 'L':
                answer += 'L'
                now_li[0] = num
            else:
                answer += 'R'
                now_li[1] = num
    return answer