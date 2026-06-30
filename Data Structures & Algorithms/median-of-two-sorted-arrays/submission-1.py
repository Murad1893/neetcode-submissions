class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2

        l, r = 0, m

        while True:
            mid1 = (l + r) // 2
            mid2 = half - mid1

            """
                1,l1(5) | r1(6), 7
                2,l2(4) | r2(8), 12

            """

            l1 = nums1[mid1-1] if mid1 > 0 else float('-inf')
            # adjacent to l1
            r1 = nums1[mid1] if mid1 < m else float('inf') 

            l2 = nums2[mid2-1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2] if mid2 < n else float('inf')

            # cross condition check
            if l1 <= r2 and l2 <= r1:
                # odd check
                if (m+n) % 2:
                    return max(l1, l2)
                return (max(l1,l2) + min(r1,r2)) / 2
            
            elif l1 > r2:
                r = mid1 - 1 # reduce search space to have lesser elements from l1
            else:
                l = mid1 + 1


            
            
            

