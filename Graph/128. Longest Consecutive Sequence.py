class Solution:
    def longestConsecutive(self, x: List[int]) -> int:
        """
        - not sorting because it is O(nlogn)
        - visualize the problem by drawing a sequence on a line in increasing order
        - the start value has no left neighbor: check through a set
        - increase by 1 to check if a sequence exist
        
        """
        numSet = set(x)
        longest = 0
        for n in x:
            #check if it is the start 
            if (n - 1) not in numSet:
                lenght = 0
                while (n + lenght) in numSet:
                    #checl current number
                    lenght += 1
                longest = max(lenght, longest)
        return longest
