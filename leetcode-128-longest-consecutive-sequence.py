class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        nums = sorted(list(set(nums)))

        k = 1
        longest = 1
        for i in range(1, len(nums)):
            if nums[i] == (nums[i - 1] + 1):
                k += 1
            else:
                k = 1
            longest = max(longest, k)
        return longest
