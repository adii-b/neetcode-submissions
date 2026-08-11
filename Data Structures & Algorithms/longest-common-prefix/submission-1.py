class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = []

        str1 = strs[0]
        str2 = strs[len(strs) - 1]
        i, j = 0, 0

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                result.append(str1[i])
                i += 1
                j += 1
            else:
                break
        
        return "".join(result)