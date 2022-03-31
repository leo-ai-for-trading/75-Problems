from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Dynamic Programming
        - cache memoization
        - start at the bottom
        - Dp- bottom up
        - two variables shifted n-1 time
        """
        f, s = 1,1
        
        for i in range(n-1):
            temp = f
            f = f+s
            s = temp
        return f
