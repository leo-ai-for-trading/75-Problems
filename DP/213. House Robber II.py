class Solution:
    def rob(self, nums: List[int]) -> int:
        #edge cases
        #skip the first and the last house
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self,nums):
        #from the prev problem
        rob1,rob2 = 0,0
        for n in nums:
            newrob = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = newrob
        return rob2
