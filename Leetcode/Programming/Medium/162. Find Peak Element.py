class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        for i in range(len(nums)):
            if nums[i] == m:
                return i
