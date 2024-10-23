def count_ways_to_make_change(coins, amount):
    # Initialize an array to store the results of subproblems
    dp = [0] * (amount + 1)
    
    # There is one way to make change for amount=0, i.e., using no coins
    dp[0] = 1

    # Iterate over each coin and update the table
    for coin in coins:
        # Iterate from the coin value to the target amount
        for i in range(coin, amount + 1):
            # Reuse the already calculated problem to update 
            # the number of ways to make change 
            dp[i] += dp[i - coin]

    return dp[amount]
