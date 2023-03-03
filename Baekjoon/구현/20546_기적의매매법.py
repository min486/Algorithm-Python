cash = int(input())
price_li = list(map(int, input().split()))

jun_cash, jun_cnt = cash, 0
sung_cash, sung_cnt = cash, 0
sung_li = []

for price in price_li:
    # BNP (준현)
    jun_cnt += jun_cash // price  # 살 수 있는만큼 매수
    jun_cash = jun_cash % price  # 매수하고 남은 돈

    # TIMING (성민)
    sung_li.append(price)
    if len(sung_li) >= 4:
        if sung_li[0] > sung_li[1] > sung_li[2]:  # 3일 연속 하락하면 다음날 가격으로 매수
            sung_cnt += sung_cash // price
            sung_cash = sung_cash % price
        elif sung_li[0] < sung_li[1] < sung_li[2]:  # 3일 연속 상승하면 다음날 가격으로 매도
            sung_cash += sung_cnt * price  # 전량 매도
            sung_cnt = 0
        sung_li.pop(0)

if jun_cash+price_li[-1]*jun_cnt > sung_cash+price_li[-1]*sung_cnt:
    print('BNP')
elif jun_cash+price_li[-1]*jun_cnt < sung_cash+price_li[-1]*sung_cnt:
    print('TIMING')
else:
    print('SAMESAME')