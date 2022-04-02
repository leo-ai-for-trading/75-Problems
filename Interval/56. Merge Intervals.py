class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        
        Reasoning
        - keep intervals in sorted orders
        - take care of the first value of the interval 
        - sort by the start value of the interval and after iterate every start value and then check if the current value overlap the previous interval and if it does we can merge them
        - O(nlogn)
        """
        
        intervals.sort(key=lambda i : i[0]) #sorting by the start value
        output = [intervals[0]]
        #avoid edge case
        
        for start,end in intervals[1:]:
            lastEnd = output[-1][1]
            if  start <= lastEnd:
                #if they are overlapping
                output[-1][1] = max(lastEnd,end)
                #because if one intervals has more larger value we need to keep the smaller value of the other intervals
            else:
                output.append([start,end])
                #example:[1,5],[7,8] = [7,8] we don't need to merge
        return output
