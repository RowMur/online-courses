def max_revenue(clicks: list, prices: list):
    clicks.sort()
    prices.sort()

    sum = 0
    for index, click in enumerate(clicks):
        sum += click * prices[index]
    
    return sum

if __name__ == "__main__":
    n_of_slots = int(input())
    clicks = list(map(int, input().split()))
    prices = list(map(int, input().split()))

    print(max_revenue(clicks, prices))