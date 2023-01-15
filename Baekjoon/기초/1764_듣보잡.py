n, m = map(int, input().split())
n_set = set()
m_set = set()

for _ in range(n):
    n_name = n_set.add(input())
for _ in range(m):
    m_name = m_set.add(input())

nm = n_set & m_set  # {'ohhenrie', 'baesangwook'}
result = sorted(nm)  # ['baesangwook', 'ohhenrie']

print(len(nm))

for i in result:
    print(i)