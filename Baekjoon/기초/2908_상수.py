a, b = input().split()
rev_a = int(a[::-1])
rev_b = int(b[::-1])

if rev_a > rev_b:
    print(rev_a)
elif rev_a < rev_b:
    print(rev_b)