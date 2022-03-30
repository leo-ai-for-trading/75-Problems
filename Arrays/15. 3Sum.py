class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        - sort input arr
        - left,right pointer
        - if the i element + left + right = 0 -> add to the solution
        - if sum > 0 shift the right pointer by - 1
        - sum < 0: shift left pointer: this increase the sum
        - https://www.youtube.com/watch?v=jzZsG8n2R9A&ab_channel=NeetCode
        """
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue #not use same value twice
            l,r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    #decrement
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1 #not having same sum
                    while nums[l] == nums[l-1] and l < r:
                        #means it's the same value
                        l += 1
        return res
