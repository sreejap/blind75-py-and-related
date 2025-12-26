# Top-down (recursion + memo)
from functools import lru_cache

@lru_cache(None)
def dp(i):
    if i == 0: return 0
    # recurrence
    res = float('inf')
    for option in options:
        res = min(res, dp(i - option) + cost)
    return res

# Bottom-up
dp = [0] * (n+1)
for i in range(1, n+1):
    for option in options:
        dp[i] = min(dp[i], dp[i-option] + cost)
