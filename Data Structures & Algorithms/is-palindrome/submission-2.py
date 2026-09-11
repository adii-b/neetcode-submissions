class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char
        newStr = newStr.lower()
        i, j = 0, len(newStr) - 1

        while i < len(newStr):
            if newStr[i] != newStr[j]:
                return False
            i += 1
            j -= 1
        
        return True