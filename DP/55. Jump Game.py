class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        - Dp
        - can we reach the last position
        - greedy solution O(n)
        - start in reverse order and check if you can reach the initial position
        - starting from the last index we check if we can make the jump of (nums[i]) to the left
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                #we can reach the goal
                #we shift the goal
                goal = i
        #if goal > 0
        return True if goal == 0 else False
        
