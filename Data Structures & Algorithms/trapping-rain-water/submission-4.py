from itertools import accumulate
class Solution:
    def trap(self, height: List[int]) -> int:
        # formulae min(L-R) - h[i] (width is 1 if you consider the same pos)
        # compute water stored at each position and sum all the water to get total

        # prefix/suffix store
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        max_left = height[0]
        max_right = height[-1]

        for i in range(1, len(height)):
            max_left = max(height[i-1], max_left)
            prefix[i] = max_left
        
        for i in range(len(height)-2,-1,-1):
            max_right = max(height[i+1], max_right)
            suffix[i] = max_right
        print(prefix)
        print(suffix)
        # now compute the trapped water at each pos
        result = 0
        for i in range(len(height)):
            h = min(prefix[i], suffix[i]) - height[i]
            result = result + h if h > 0 else result

        return result 