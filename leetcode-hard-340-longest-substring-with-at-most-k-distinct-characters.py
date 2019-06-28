class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k): # :type s: str :type k: int :rtype: int
        n, last, best, earliest = len(s), {}, 0, -1
        if k == 0 or n == 0: return 0
        for i, ch in enumerate(s):
            if len(last) == k and ch not in last:
                earliest = min(last.values())
                to_remove = s[earliest]
                del last[to_remove]
            last[ch] = i
            best = max(best, i - earliest)
        return best
