class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr = sorted(arr)
        if len(arr) % 2 == 0:
            l = int(len(arr) / 2)
            ans = (arr[l - 1] + arr[l]) / 2
            return ans
        else:
            l = len(arr) // 2
            return arr[l]

