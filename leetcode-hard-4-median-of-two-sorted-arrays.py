class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        l = len(nums)
        if l % 2 is 0:
            return (nums[int(l/2)] + nums[int(l/2) - 1]) / 2
        else:
            return nums[int(l/2)]

