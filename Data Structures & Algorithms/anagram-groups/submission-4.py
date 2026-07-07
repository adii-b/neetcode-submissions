class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        freq_map = defaultdict(list)

        for string in strs:
            freq_array = [0] * 26
            for char in string:
                freq_array[ord(char) - ord('a')] += 1
            t = tuple(freq_array)
            if t in freq_map:
                freq_map[t].append(string)
            else:
                freq_map[t] = [string]
        
        for k in freq_map:
            result.append(freq_map[k])
        
        return result
            


        