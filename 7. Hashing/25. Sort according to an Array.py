class Solution:
    def relativeSort(self, A1, A2):
        freq = {}
        res = []
        
        for num in A1:
            freq[num] = freq.get(num, 0) + 1
        
        for num in A2:
            while num in freq and freq[num] > 0:
                res.append(num)
                freq[num] -= 1
            
            if num in freq:
                del freq[num]
        
        remaining = []
        for key, count in freq.items():
            remaining.extend([key] * count)
        
        remaining.sort()
        res.extend(remaining)
        
        return res