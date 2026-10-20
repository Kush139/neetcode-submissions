class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_so_far = nums[0]
        max_sum_so_far = nums[0]

        for i in range(1, len(nums)):
            sum_so_far = max(nums[i], sum_so_far + nums[i])
            max_sum_so_far = max(max_sum_so_far, sum_so_far)
        return max_sum_so_far