li = [2, 3, 5, 7, 11]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    cnt = [0] * len(li)  # 거듭제곱을 세기 위한 리스트 
    
    for i in range(len(li)):
        # 소수가 나올때까지 계속 소수로 나누기
        while True:
            if n % li[i] == 0:
                cnt[i] += 1
                n //= li[i]
            else:
                break
    # int 형으로 구성된 리스트를 join하면 에러 발생하므로
    # str 형으로 변경
    result = " ".join(map(str, cnt))
    print(f'#{tc} {result}')