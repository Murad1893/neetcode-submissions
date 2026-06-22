class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-1):
            # make sure to check prev once i is not at the first position!
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # remove duplicates
                    while l < r and nums[l] == nums[l-1]: l+=1
                    while l < r and nums[r] == nums[r+1]: r-=1

        return result