class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] = max amount of money 
        if len(nums) == 1:
            return nums[0]
        two_back = nums[0]
        one_back = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = one_back
            one_back = max(two_back+nums[i], one_back)
            two_back = tmp

        return one_back




