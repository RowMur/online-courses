def money_change(money):
    n_of_coins = 0
    coins = [10, 5, 1]

    while money:
        for coin in coins:
            if money >= coin:
                money -= coin
                n_of_coins += 1
                break
    
    return n_of_coins


if __name__ == "__main__":
    money = int(input())
    print(money_change(money))