class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        - find the subproblem
        - find the max of subarray
        - rob(max(arr[0] + rob[2:], rob[1:]))
        - look at the previous result we have computed
        - 
        """
        rob1, rob2 = 0,0
        
        #[rob1, rob2, n, n+1, n+2,...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp #it is the n in the example above
        return rob2 #it is the max
