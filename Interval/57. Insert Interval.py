class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        - iterate through the sorted interval and find the insertion point of the invterval we are looking for
        - add the new interval to the result 
        - if they are not overlapping we merge by the min of the left interval and the max of the right interval
        """
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            #interval stil overlapping to the right
            elif  newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                #update the interval
                newInterval = [min(newInterval[0], intervals[i][0]),max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval) 
        
        return res
