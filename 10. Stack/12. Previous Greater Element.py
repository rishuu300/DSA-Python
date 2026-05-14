class Solution:
    def preGreaterEle(self, arr):
        n = len(arr)
        stack = []
        prevs = [0] * n
        
        stack.append(0)
        prevs[0] = -1
        
        for i in range(1, n):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            
            prevs[i] = arr[stack[-1]] if stack else -1
            
            stack.append(i)
        
        return prevs