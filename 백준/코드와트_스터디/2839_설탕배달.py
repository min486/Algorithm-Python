gram = int(input())
min_cnt = 0

while gram > 0:
    if gram % 5 == 0:  # 5의 배수면 몫 추가
        min_cnt += (gram // 5)
        print(min_cnt)
        break
    gram -= 3  # 5의 배수 아니면 3kg 감소, 개수 1 추가
    min_cnt += 1

    if gram == 0:  # 3의 배수면 0 이됨
        print(min_cnt)
        break

else:
    print(-1)