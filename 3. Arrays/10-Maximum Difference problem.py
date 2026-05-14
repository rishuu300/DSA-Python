def maxDiff(arr):
    n = len(arr)
    ans = -1
    mini = arr[0]
    
    for i in range(1, n):
        if arr[i] <= mini:
            mini = arr[i]
        else:
            ans = max(ans, arr[i] - mini)
    
    return ans