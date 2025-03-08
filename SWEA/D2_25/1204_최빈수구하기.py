t = int(input())

for tc in range(1, t+1):
    _ = input()
    li = list(map(int, input().split()))
    cnt_li = [0] * 101
    max_cnt, answer = 0, 0

    for i in li:
        cnt_li[i] += 1

    for j in range(len(cnt_li)):
        if cnt_li[j] >= max_cnt:
            max_cnt = cnt_li[j]
            answer = j

    print(f'#{tc} {answer}')