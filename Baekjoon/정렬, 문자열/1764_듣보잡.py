n, m = map(int, input().split())
n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())

# set 교집합
nm = n_set & m_set  # {'ohhenrie', 'baesangwook'}
result = sorted(nm)  # ['baesangwook', 'ohhenrie']
print(len(result))

for i in result:
    print(i)