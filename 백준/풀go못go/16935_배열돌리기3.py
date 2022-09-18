n, m, a = map(int, input().split())
old = [list(map(int, input().split())) for _ in range(n)]
nums = list(map(int, input().split()))

def rotate1(old):
    n = len(old)
    m = len(old[0])
    new = list([0] * m for _ in range(n))
    
    for i in range(n):
        for j in range(m):
            new[i][j] = old[n-i-1][j]
    return new

def rotate2(old):
    n = len(old)
    m = len(old[0])
    new = list([0] * m for _ in range(n))
    
    for i in range(n):
        for j in range(m):
            new[i][j] = old[i][m-j-1]
    return new

def rotate3(old):
    n = len(old)
    m = len(old[0])
    new = list([0] * n for _ in range(m))
    
    for i in range(m):
        for j in range(n):
            new[i][j] = old[n-j-1][i]
    return new

def rotate4(old):
    n = len(old)
    m = len(old[0])
    new = list([0] * n for _ in range(m))
    
    for i in range(m):
        for j in range(n):
            new[i][j] = old[j][m-i-1]
    return new

def rotate5(old):
    n = len(old)
    m = len(old[0])
    half_n = n // 2
    half_m = m // 2
    new = list([0] * m for _ in range(n))
    
    for i in range(half_n):
        for j in range(half_m):
            # 1 -> 2
            new[i][j+half_m] = old[i][j]
            # 2 -> 3
            new[i+half_n][j+half_m] = old[i][j+half_m]
            # 3 -> 4
            new[i+half_n][j] = old[i+half_n][j+half_m]
            # 4 -> 1
            new[i][j] = old[i+half_n][j]
    return new

def rotate6(old):
    n = len(old)
    m = len(old[0])
    half_n = n // 2
    half_m = m // 2
    new = list([0] * m for _ in range(n))
    for i in range(half_n):
        for j in range(half_m):
            # 1 -> 4
            new[i+half_n][j] = old[i][j]
            # 4 -> 3
            new[i+half_n][j+half_m] = old[i+half_n][j]
            # 3 -> 2
            new[i][j+half_m] = old[i+half_n][j+half_m]
            # 2 -> 1
            new[i][j] = old[i][j+half_m]
    return new

func = [rotate1, rotate2, rotate3, rotate4, rotate5, rotate6]

for num in nums:
    old = func[num-1](old)

for row in old:
    print(*row, sep=' ')