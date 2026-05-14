from collections import Counter
import heapq

class Solution:
    def kMostFrequent(self, arr, n, k) :
        freq = Counter(arr)
        heap = []
        
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        total = 0
        
        while heap:
            count, num = heapq.heappop(heap)
            
            total += freq[num]
        
        return total