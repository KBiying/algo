import sys


class Solution(object):
    def isCover(self, substr, t):
        for item in t:
            if item not in substr:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        left, right = 0, 0
        valid = False
        min_len = sys.maxint
        while right < len(s):
            # record s[right]
            a = s[right]
            right += 1
            valid = self.isCover(s[left:right], t)
            while valid:
                temp_len = right - left
                if temp_len < min_len:
                    min_len = temp_len
                d = s[left]
                left += 1
                valid = self.isCover(s[left:right], t)
