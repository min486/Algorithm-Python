T = int(input())

for tc in range(T):
    N = int(input())
    persons = [list(map(int, input().split())) for _ in range(N)]
    persons.sort()  # 서류 순위 기준 오름차순 정렬

    min_rank = persons[0][1]  # 첫번째 지원자의 면접 순위
    cnt = 1

    for i in range(1, N):
        # 지원자의 면접 순위가 전까지 저장된 가장 높은 순위보다 더 높을시
        if persons[i][1] < min_rank:  
            cnt += 1
            min_rank = persons[i][1]

    print(cnt)
