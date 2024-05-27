def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Initialize the minimum coins needed for each amount from 0 to amount
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    # Initialize a list to keep track of the last coin used to form each amount
    last_coin = [-1] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                last_coin[x] = coin
    
    # Construct the result using the last_coin array
    result = {}
    while amount > 0:
        coin = last_coin[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result
