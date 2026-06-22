class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # area = 0
        
        # for l in range(len(heights)):
        #     for r in range(l+1, len(heights)):
        #         area = max(area, min(heights[l], heights[r]) * (r-l))

        # return area
        l, r = 0, len(heights) - 1
        area = 0 

        while l < r:
            area = max(area, min(heights[l], heights[r]) * (r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area