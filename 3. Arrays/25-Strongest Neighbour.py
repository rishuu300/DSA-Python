class Solution:
    def strongestNeighbour(self, arr):
        res = [max(arr[i], arr[i + 1]) for i in range(len(arr) - 1)]
        return res