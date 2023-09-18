class Solution(object):
    def isCover(self, window, need_dict):
        window_dict = {}
        for ii in need_dict:
            window_dict[ii] = 0
        for item in window:
            if window_dict.get(item) != None:
                window_dict[item] += 1
        for ii in need_dict:
            if need_dict[ii] > window_dict[ii]:
                return False
        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        left, right = 0, 0
        valid = False
        need_dict = {}
        for item in s1:
            if need_dict.get(item) == None:
                need_dict[item] = 1
            else:
                need_dict[item] += 1
        print(need_dict)

        while right < len(s2):
            a = s2[right]
            right += 1
            valid = self.isCover(s2[left:right], need_dict)
            while valid:
                temp_len = right - left
                if temp_len == len(s1):
                    return True
                d = s2[left]
                left += 1
                valid = self.isCover(s2[left:right], need_dict)
        return False
