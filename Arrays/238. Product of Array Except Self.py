import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #default value of 1 in the first place
        res = [1] * (len(nums))
        #multiply i*i+1
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            #populate the arr
            pref *= nums[i]
        #multiply nums[-1]*nums[-2] and so on
        postf = 1
        for i in range(len(nums) -1, -1, -1):
            #start from the end
            #populate the arr
            res[i] *= postf
            postf *= nums[i]
        return res

        
