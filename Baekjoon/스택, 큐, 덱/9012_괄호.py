n = int(input())

for _ in range(n):
    line = list(input())
    open = 0

    for i in line:
        if i == '(':
            open += 1
        else:
            open -= 1
            if open < 0 :
                print("NO")
                break
    # for문이 break 없이 완료되면 작동
    else :
        if open == 0:
            print("YES")
        else:
            print("NO")