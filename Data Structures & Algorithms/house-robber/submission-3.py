class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] = max amount of money 
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = {}
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[2]+nums[0], nums[1])

        for i in range(3, len(nums)):
            
            dp[i] = max(dp[i-2]+nums[i], nums[i-1], dp[i-3]+nums[i])
        last = len(nums) - 1
        sl = len(nums) - 2
        return max(dp[last], dp[sl])




