class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {i: 1 for i in range(len(nums))}
        #dp[i] = longest sequence
        for i in range(len(nums)-1,-1,-1):
            to_beat = nums[i]
            for j in range(i, len(nums)):
                if nums[j] > to_beat:
                    dp[i] = max(dp[i], 1+dp[j])
    
        return max(dp.values())

            
        