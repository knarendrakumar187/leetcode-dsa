class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1













            # LeetCode 88 - Merge Sorted Array
#
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
#
# Initial
#
# nums1: [1][2][3][0][0][0]
#              ↑        ↑
#              m-1      last
#
# nums2: [2][5][6]
#              ↑
#              n-1
#
# ------------------------------------------------
#
# Step 1
# Compare: 3 vs 6
#
# nums1: [1][2][3][0][0][6]
#              ↑     ↑
#              m-1   last
#
# nums2: [2][5][6]
#          ↑
#          n-1
#
# ------------------------------------------------
#
# Step 2
# Compare: 3 vs 5
#
# nums1: [1][2][3][0][5][6]
#              ↑  ↑
#              m-1 last
#
# nums2: [2][5][6]
#      ↑
#      n-1
#
# ------------------------------------------------
#
# Step 3
# Compare: 3 vs 2
#
# nums1: [1][2][3][3][5][6]
#          ↑ ↑
#        m-1 last
#
# nums2: [2][5][6]
#      ↑
#      n-1
#
# ------------------------------------------------
#
# Step 4
# Compare: 2 vs 2
#
# nums1: [1][2][2][3][5][6]
#
# nums2 finished ✅
#
# Memory:
#
# m-1 → Last valid element in nums1
# n-1 → Last element in nums2
# last → Last empty position in nums1
#
# Compare nums1[m-1] and nums2[n-1]
# Bigger element → nums1[last]
# Move that pointer
# last--
# Repeat
#
# Copy remaining nums2 elements (if any)
#
# Time : O(m + n)
# Space: O(1)