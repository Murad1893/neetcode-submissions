from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        sorted_x = sorted(x, key=lambda k: -x[k])
        return list(sorted_x[:k])