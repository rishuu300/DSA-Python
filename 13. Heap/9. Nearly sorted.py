import heapq

class Solution:
    def nearlySorted(self, arr, k):
        n = len(arr)
        
        heap = []
        
        for i in range(k):
            heapq.heappush(heap, arr[i])
        
        index = k
        
        while index < n:
            heapq.heappush(heap, arr[index])
            
            arr[index - k] = heapq.heappop(heap)
            
            index += 1
        
        while heap:
            arr[index - k] = heapq.heappop(heap)
            index += 1