class Solution:
    def longestUniqueSubstr(self, s):
        n = len(s)
        prev = [-1] * 26
        index, res = 0, 0
        
        for i in range(n):
            char_index = ord(s[i]) - ord('a')
            index = max(index, prev[char_index] + 1)
            maxEnd = i - index + 1
            res = max(res, maxEnd)
            prev[char_index] = i
        
        return res