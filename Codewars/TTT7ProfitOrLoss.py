def profitLoss(records):
    total_profit = 0
    for (sell_price, profit_percent) in records:
        original = sell_price/(1+(profit_percent/100))
        total_profit += sell_price - original
    return round(total_profit, 2)
