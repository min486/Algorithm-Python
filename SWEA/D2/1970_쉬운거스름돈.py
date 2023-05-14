li = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    print(f'#{tc}')

    for i in li:
        div = n // i
        n -= (i * div) 
        print(div, end = ' ')            
    print()