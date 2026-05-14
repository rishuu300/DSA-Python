def distinct(arr):
    s = set()
    
    for i in range(len(arr)):
        s.add(arr[i])
    
    return len(s)