class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        l = len(nums)
        for i in range(0,l-1):
            for j in range(i+1,l):
                if i < j:
                    arr.append(nums[j]-nums[i])
        if max(arr) <= 0:
            return -1
        else:
            return max(arr)