class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {} # maintain char and last_seen_index
        l = 0
        result = 0

        for r in range(len(s)):
            if s[r] in char_dict and char_dict[s[r]] >= l:
                # update left to last seen idx
                l = char_dict[s[r]] + 1
            char_dict[s[r]] = r
            result = max(result, r - l + 1)

        return result