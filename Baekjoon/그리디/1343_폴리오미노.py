put = input()
put = put.replace('XXXX', 'AAAA')
put = put.replace('XX', 'BB')

# X가 남아 있으면 (덮을 수 없으면)
if 'X' in put:
    print(-1)
else:
    print(put)