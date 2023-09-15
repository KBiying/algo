import sys


class Solution(object):
    def isCover(self, window, need_dict):
        # calculate the times of appearing in need
        # print(window)
        window_dict = {}
        for ii in need_dict:
            window_dict[ii] = 0
        for item in window:
            if window_dict.get(item) != None:
                window_dict[item] += 1
        # print(window_dict)
        for ii in need_dict:
            if need_dict[ii] > window_dict[ii]:
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
        min_len = 500000
        min_substr = ""
        need_dict = {}
        for item in t:
            if need_dict.get(item) == None:
                need_dict[item] = 1
            else:
                need_dict[item] += 1
        print(need_dict)
        if len(t) > len(s):
            return min_substr
        while right < len(s):
            # record s[right]
            a = s[right]
            right += 1
            valid = self.isCover(s[left:right], need_dict)
            while valid:
                temp_len = right - left
                if temp_len < min_len:
                    min_len = temp_len
                    min_substr = s[left:right]
                d = s[left]
                left += 1
                valid = self.isCover(s[left:right], need_dict)

        return min_substr

    def run(self):
        r = self.minWindow(
            "AABC",
            "BA",
        )
        print(r)


mycase = Solution()
mycase.run()
