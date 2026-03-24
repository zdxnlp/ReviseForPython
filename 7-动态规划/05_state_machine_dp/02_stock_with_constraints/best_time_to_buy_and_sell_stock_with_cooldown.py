def max_profit_with_cooldown(prices: list[int]) -> int:
    if not prices:
        return 0

    # Step 1: 定义状态
    hold = -prices[0]
    sold = 0
    rest = 0

    # Step 2 and 3: 状态转移
    for price in prices[1:]:
        prev_hold, prev_sold, prev_rest = hold, sold, rest
        hold = max(prev_hold, prev_rest - price)
        sold = prev_hold + price
        rest = max(prev_rest, prev_sold)

    # Step 4: 返回答案
    return max(sold, rest)


if __name__ == "__main__":
    print(max_profit_with_cooldown([1, 2, 3, 0, 2]))
