n = int(input())
soon = list(map(int, input().split()))
i = n - 2

while 0 <= i:
    if soon[i] > soon[i + 1]:  # 바꿀 수 있는 가장 낮은 자릿수부터 탐색 
        break
    else:
        i -= 1  # 자릿수 앞으로 이동하도록 인덱스 감소

if i == -1:  # n = 1인 경우 or 사전순 가장 처음일 때
    print(-1)
    
else:
    for j in range(i+1, len(soon)):
        if soon[i] > soon[j]:  # i보다 작되, 가장 낮은 자릿수 탐색
            jj = j

    soon[i], soon[jj] = soon[jj], soon[i]  # 두 수 위치 변경

    align = soon[i + 1:]  # i보다 낮은 자릿수들 정렬
    align.sort(reverse = True)

    print(' '.join(map(str, (soon[:i + 1] + align))))
    