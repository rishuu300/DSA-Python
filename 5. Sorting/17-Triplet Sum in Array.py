class Solution:
    def hasTripletSum(self, arr, target):
        n = len(arr)
        arr.sort()
        
        for i in range(n-2):
            low, high = i+1, n-1
            
            while low < high:
                total_sum = arr[i] + arr[low] + arr[high]
                
                if total_sum == target:
                    return True
                elif total_sum < target:
                    low += 1
                else:
                    high -= 1
        
        return False