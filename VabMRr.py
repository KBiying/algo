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

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        left, right = 0, 0
        valid = False
        need_dict = {}
        return_list = []
        for item in p:
            if need_dict.get(item) == None:
                need_dict[item] = 1
            else:
                need_dict[item] += 1

        while right < len(s):
            a = s[right]
            right += 1
            valid = self.isCover(s[left:right], need_dict)
            while valid:
                temp_len = right - left
                if temp_len == len(p):
                    return_list.append(left)
                d = s[left]
                left += 1
                valid = self.isCover(s[left:right], need_dict)
        return return_list
