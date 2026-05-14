class Solution(object):
    def subsetsWithDup(self, arr):
        res = []
        arr.sort()
        self.solve(arr, 0, res, [])
        return res

    def solve(self, arr, index, res, curr_list):
        res.append(curr_list[:])

        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i-1]:
                continue
            curr_list.append(arr[i])
            self.solve(arr, i+1, res, curr_list)
            curr_list.pop()