class Solution:
    def numDecodings(self, s: str) -> int:
        """
        - string from 1 to 9 not including 0
        - if it start with 1 u can take every number from 0 to 9 otherwise if it starts with 2 we can only take from 0 to 6
        - 
        """
        dp = {len(s) :  1}
        
        for i in range(len(s) - 1,- 1,- 1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        return dp[0]
    
        dp = {len(s): 1}
        def dfs(i):
            if i in dp:
                #base case
                return dp[i]
            if s[i] == "0":
                #can't decode the string
                return 0
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i +1] in "0123456")):
                #checking if in 10 to 26
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)               
