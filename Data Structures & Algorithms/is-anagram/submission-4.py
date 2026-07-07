class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h = {}

        for char in s:
            h[char] = h.get(char, 0) + 1
        
        for char in t:
            h[char] = h.get(char, 0) - 1
        
        for key in h:
            if h[key] != 0:
                return False
        
        return True