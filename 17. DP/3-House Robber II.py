class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]

        # return max(self.memo(nums1, 0, {}, n-1), self.memo(nums2, 0, {}, n-1))
        # return max(self.table(nums1, n-1), self.table(nums2, n-1))
        return max(self.space(nums1, n-1), self.space(nums2, n-2))
    
    def memo(self, nums, index, memo, n):
        if index >= n:
            return 0
        
        if index in memo:
            return memo[index]

        skip = self.memo(nums, index+1, memo, n)
        take = nums[index] + self.memo(nums, index+2, memo, n)

        return max(skip, take)
    
    def table(self, nums, n):
        dp = [0]*n
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-2], nums[n-1])

        for i in range(n-3, -1, -1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        
        return dp[0]
    
    def space(self, nums, n):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr