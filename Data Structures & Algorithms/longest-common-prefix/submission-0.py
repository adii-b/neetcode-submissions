class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = []

        i, j = 0, 0

        while i < len(strs[0]) and j < len(strs[-1]):
            if strs[0][i] == strs[-1][j]:
                result.append(strs[0][i])
                i += 1
                j += 1
            else:
                return "".join(result)
        
        return "".join(result)
        