class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        arr = sorted(nums)
        if len(arr)<2:
            return 0
        else:
            res = []
            for i in range(len(arr)-1):
                res.append(arr[i+1]-arr[i])
        return max(res)