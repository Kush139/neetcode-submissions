class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] = max amount of money 
        if len(nums) == 1:
            return nums[0]
        dp = {}
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        last = len(nums) - 1
        sl = len(nums) - 2
        return max(dp[last], dp[sl])




