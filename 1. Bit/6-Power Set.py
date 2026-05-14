class Solution:
    def AllPossibleStrings(self, s):
        n = len(s)
        subsequences = []
        
        for mask in range(1, 2 ** n):
            sequence = ""
            for j in range(n):
                if mask & (1 << j):
                    sequence += s[j]
            subsequences.append(sequence)
        
        subsequences.sort()
        return subsequences