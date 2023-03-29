gram = int(input())
min_cnt = 0

while gram > 0:
    # 5의 배수면 몫 추가
    if gram % 5 == 0:
        min_cnt += (gram // 5)
        print(min_cnt)
        break
    # 5의 배수 아니면 3kg 감소, 개수 1 추가
    gram -= 3
    min_cnt += 1

    # 3의 배수면 0이 된다
    if gram == 0:  
        print(min_cnt)
        break
else:
    print(-1)