from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26
        l = 0

        if len(s2) < len(s1): return False

        for char in s1:
            freq_s1[ord(char) - ord('a')] += 1
        
        for i in range(len(s1)):
            freq_s2[ord(s2[i]) - ord('a')] += 1

        for r in range(len(s1), len(s2)):
            if freq_s1 == freq_s2: return True

            freq_s2[ord(s2[r]) - ord('a')] += 1
            freq_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return freq_s1 == freq_s2




