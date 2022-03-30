class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        - pointer left, right
        - shift left pointer + 1
        - if area is smaller shift pointer
        - https://www.youtube.com/watch?v=UuiTKBwPgAo&ab_channel=NeetCode
        """
        res = 0
        l,r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l],height[r])
            res = max(res,area)
            
            if height[l] < height[r]:
                #maximize both heights
                l += 1

            else:
                r -= 1
        return res
                
