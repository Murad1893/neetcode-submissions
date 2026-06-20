class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += "#"
            for char in s:
                result += char
        
        return result
                
    def decode(self, s: str) -> List[str]:
        i = 0
        length = ""
        result = []
        
        while i < len(s):
            if s[i] == "#":
                size = int(length)
                j = i + 1
                temp = ""
                while j < size + (i+1):
                    temp += s[j]
                    j += 1
                result.append(temp)

                i += size
                length = ""
            else:
                length += s[i]
            i += 1

        return result