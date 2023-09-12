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
        while right < len(nums):
            a = nums[right]
            right += 1
            sum += a

            print("window[%d, %d]".format(left, right))
            while sum >= target:
                d = nums[left]
                left += 1
