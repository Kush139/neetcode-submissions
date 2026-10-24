class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_now = nums[0]
        min_now = nums[0]
        max_so_far = max_now

        for i in range(1,len(nums)):
            if nums[i] == 0:
                max_now, min_now = 0, 0
            tmp = max_now
            max_now = max(nums[i], nums[i]*max_now, nums[i]*min_now)
            min_now = min(nums[i], nums[i]*min_now, nums[i]*tmp)
            max_so_far = max(max_so_far, max_now)
        return max_so_far




        