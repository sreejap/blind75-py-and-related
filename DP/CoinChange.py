from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache (None)
        def dfs (rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_cost = float ('inf')
            for c in coins:
                cost = dfs (rem-c)
                if cost != -1:
                    min_cost = min (min_cost, cost+1)
            return min_cost if min_cost != float('inf') else -1

        return dfs (amount)
