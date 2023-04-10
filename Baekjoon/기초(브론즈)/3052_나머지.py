se = set()

for _ in range(10):
    num = int(input())
    se.add(num % 42)

print(len(se))