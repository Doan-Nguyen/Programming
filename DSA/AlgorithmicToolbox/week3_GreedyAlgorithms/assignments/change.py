def change(money):
    # sorted by value
    dict_coins_value = [{"value": 10}, {"value": 5}, {"value": 1}]
    total_coins = 0
    for coin_value in dict_coins_value:
        total_coins += int(money/coin_value["value"])
        money = money - int(money/coin_value["value"])*coin_value["value"]
    return total_coins


if __name__ == "__main__":
    money = int(input())
    total_coins = change(money)
    print(total_coins)