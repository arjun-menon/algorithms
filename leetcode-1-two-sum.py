class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            wanted = target - num
            if wanted in seen:
                j = seen[wanted]
                return [i, j] if i < j else [j, i]
            
            seen[num] = i
