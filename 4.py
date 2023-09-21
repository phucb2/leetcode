class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        
        while i < m:
            nums.append(nums1[i])
            i += 1
        while j < n:
            nums.append(nums2[j])
            j += 1
        
        if (m + n) % 2 != 0:
            return nums[(m + n) // 2]
        else:
            return (nums[(m + n)//2] + nums[(m+n)//2 - 1])*0.5
