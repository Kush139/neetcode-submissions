class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(num_list):
            if not num_list:
                return 0
            if len(num_list) == 1:
                return num_list[0]
            two_back = num_list[0]
            one_back = max(two_back, num_list[1])
            for i in range(2,len(num_list)):
                tmp = one_back
                one_back = max(two_back+num_list[i], one_back)
                two_back = tmp
            return one_back
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

        