class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
           2---3
        1--2   3--4 
        the above is the edge case
        - if the second start after the end of the first they are not overlapping
        - remove the one it ends first to avoid overlapping
        - sort the array and compare the json pair
        - keep tracking the end value of the first interval
        
        """
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            #not overlap if
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end,prevEnd)
        return res
