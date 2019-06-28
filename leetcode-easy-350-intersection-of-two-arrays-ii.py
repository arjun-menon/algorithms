class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def set_and_freq(nums):
            s = set(nums)
            f = {x: 0 for x in s}
            for x in nums:
                f[x] += 1
            return s, f
        s1, f1 = set_and_freq(nums1)
        s2, f2 = set_and_freq(nums2)
        result = []
        for x in s1 & s2:
            f = min(f1[x], f2[x])
            result.extend([x] * f)
        return result

