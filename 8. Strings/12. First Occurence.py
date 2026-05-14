class Solution:
    def firstOccurence(self, txt, pat):
        n = len(txt)
        m = len(pat)
        
        for i in range(n - m + 1):
            
            j = 0
            while j < m and txt[i + j] == pat[j]:
                j += 1
            
            if j == m:
                return i
        
        return -1