class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # O(1) space because O(26) finite english chars
        
        char_freq = [0] * 26
        for char in s:
            char_freq[ord(char) - ord('a')] += 1

        for char in t:
            if not char_freq[ord(char) - ord('a')]:
                return False
            char_freq[ord(char) - ord('a')] -= 1
        
        return True
