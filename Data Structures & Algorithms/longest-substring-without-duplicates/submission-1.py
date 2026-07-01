class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        using a set() wrong because we don't know if duplicate get's
        removed if s[l] is popped (so we'd need a while)
        """

        char_set = set()
        l = 0 
        result = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1 
            char_set.add(s[r])
            result = max(result, r - l + 1)

        return result