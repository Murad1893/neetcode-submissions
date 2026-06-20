class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result
                
    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        length = ""
        result = []
        
        while i < len(s):
            j = i
            
            while s[j] != "#":
                # traverse up until delimiter
                j += 1
            # use slicing instead of appending
            length = int(s[i:j])
            j += 1 # to move past delimiter
            result.append(s[j:j+length]) # append the string up until length of chars
            i = j + length # increment i to the next length

        return result