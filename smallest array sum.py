import sys
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        valid = 0
        sum = 0
        min_len = sys.maxint
        # right is useless
        while right < len(nums):
            a = nums[right]
            right += 1
            sum += a
                
            print("window[%d, %d)".format(left, right))

            while sum >= target:
                
                temp_len = right - left
                if temp_len < min_len:
                    min_len = temp_len

                d = nums[left]
                left += 1
                sum -= d
                
                
                
