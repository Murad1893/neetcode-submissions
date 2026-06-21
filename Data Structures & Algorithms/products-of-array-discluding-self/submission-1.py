class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        num_len = len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i-1]
            
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffix[i] = nums[i]
            else:
                suffix[i] = nums[i] * suffix[i+1]

        for i in range(len(prefix)):
            p = 1 if i == 0 else prefix[i-1]
            s = 1 if i == len(suffix) - 1 else suffix[i+1]

            nums[i] = p * s

        return nums
