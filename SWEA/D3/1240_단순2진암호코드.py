dic = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

def solve():
    for st in arr:
        if '1' in st:
            # 오른쪽끝의 '1'찾기
            e = len(st)-1
            while st[e]=='0':
                e -= 1

            # 7개씩 암호 읽어오기
            result = []
            for i in range(e-55, e+1, 7):
                result.append(dic[st[i:i+7]])

            # 확인해서 정상이면 값 리턴, 아니면 0
            if (sum(result[0:8:2])*3 + sum(result[1:8:2])) % 10 == 0:
                return sum(result)
            else:
                return 0

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    result = solve()
    print(f'#{tc} {result}')