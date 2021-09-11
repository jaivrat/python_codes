
import math
import os
import random
import re
import sys


# Dynamic programming - coins denominations ways

def solve(n, coins):
    # Write your code here
    # coins.sort(reverse = False)
    def solve_helper(n, coin_denom, coins_counts, coin_idx):
        # If all done and yet coins there or just finished => success
        if n == 0 and (coin_idx <= len(coins_counts)):
            return 1
        # If need more/bigger denomination left and no coins left => fail
        if coin_idx >= len(coins_counts) and n!=0:
            return 0
        
        total_ways = 0
        # include
        coin = coin_denom[coin_idx]
        # 0 means exclude
        for cnt in range(0, coins_counts[coin_idx]+1, 1):
            total_ways = total_ways + solve_helper(n-cnt * coin, 
                                                    coin_denom, 
                                                    coins_counts, coin_idx+1)
        return total_ways


if __name__ == '__main__':
    ways = solve(15, [2 ,3 ,1 ,1])
    print(ways)
    print("Exiting...")
