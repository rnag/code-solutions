"""
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

Links:
    - https://leetcode.com/problems/coin-change/
    - https://youtu.be/H9bfqozjoqs

"""
from __future__ import annotations

__all__ = ['coin_change']


def coin_change(coins: list[int], amount: int) -> int:
    # initially fill array with an invalid # of coins - we use
    # `amount + 1` because that's impossible (max is `amount`)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            # current `amount` minus the `coin`, we want to check if
            # we can use the coin to sum to the amount
            diff = a - c

            if diff >= 0:
                dp[a] = min(dp[a], 1 + dp[diff])

    num_coins = dp[amount]
    return num_coins if num_coins != amount + 1 else -1
