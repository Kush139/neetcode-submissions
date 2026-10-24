class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_yet = nums[0]
        min_yet = nums[0]
        max_so_far = max_yet

        for i in range(1,len(nums)):
            if nums[i] == 0:
                max_yet, min_yet = 0, 0
            tmp = max_yet
            max_yet = max(nums[i], nums[i]*max_yet, nums[i]*min_yet)
            min_yet = min(nums[i], nums[i]*min_yet, nums[i]*tmp)
            max_so_far = max(max_so_far, max_yet)
        return max_so_far




        