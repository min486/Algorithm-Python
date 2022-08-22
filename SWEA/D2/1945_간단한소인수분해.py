T = int(input())

soinsu = [2, 3, 5, 7, 11]

for tc in range(1, T + 1):
    N = int(input())
    # 거듭제곱을 세기 위한 리스트 초기화 
    cnt = [0] * len(soinsu)
    
    for i in range(len(soinsu)):
        # 소수가 나올때까지 계속 소수로 나누어주기 위해 while 사용
        while True:
            if N % soinsu[i] == 0:
                # 나누어진 소수의 위치에 1씩 추가 할당
                cnt[i] += 1
                N //= soinsu[i]
            else:
                break
    # int 형으로 구성된 리스트를 join하면 에러 발생하므로
    # str 형으로 변경
    result = " ".join(map(str, cnt))
    print(f'#{tc} {result}')