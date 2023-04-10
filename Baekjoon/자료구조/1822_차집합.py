a, b = input().split()
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

result = list(a_set - b_set)

print(len(result))
print(*sorted(result))