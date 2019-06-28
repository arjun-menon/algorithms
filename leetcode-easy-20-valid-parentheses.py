class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        br = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in br.keys():
                stack.append(c)
            elif c in br.values():
                if not stack:
                    return False
                if c != br[stack.pop()]:
                    return False
        return not stack
