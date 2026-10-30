class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            rest= target - nums[i]
            if rest in nums[i+1:]:
                j = i + 1 + nums[i+1:].index(rest)
                return [i, j]
    
            

            


        
        