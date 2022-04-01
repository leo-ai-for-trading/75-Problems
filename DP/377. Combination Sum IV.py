class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        - using cache 1D
        - remaining will be put in the cache
        - bottom up memoisation
        """
        dp = {0 : 1}
        #FIRST IS THE BASE CASE
        
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                #looking at subprob
                dp[total] += dp.get(total - n,0) #avoid negative numb
        return dp[target]
