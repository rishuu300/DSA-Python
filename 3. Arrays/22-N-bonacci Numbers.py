def bonacciseries(n, m):
    arr = [0]*m
    arr[n - 1] = 1
    arr[n] = 1

    for i in range(n + 1, m):
        arr[i] = 2 * arr[i - 1] - arr[i - n - 1]
    
    return arr