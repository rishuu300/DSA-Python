def maxEvenOdd(arr, n):
    if (n == 0):
        return 0

    maxLength = 0
    
    prevOdd = arr[0] % 2
    curLength = 1

    for i in range(1, n):
        if (arr[i] % 2 != prevOdd):
            curLength += 1
        else:
            curLength = 1
        
        if (curLength > maxLength):
            maxLength = curLength

        prevOdd = arr[i] % 2
        
    return maxLength