class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(list(set(nums)))
        if len(s)<3:
            return max(s)
        else:
            return s[-3]
