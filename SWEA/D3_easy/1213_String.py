t = 10

for tc in range(1, t+1):
    _ = input()
    find = input()
    st = input()
    
    result = st.count(find)

    print(f'#{tc} {result}')