class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #dp[len(cost)-1] = cost[-1]
        #dp[len(cost)-2] = cost[-2]
        #dp[i] = min(cost[i+1), cost[i+2]
        #dp[i] = min cost to get to top from there

        #dp[i] = min cost to reach step i
        one = 0
        two = 0

        for i in range(2,len(cost)):
            tmp = one
            one = min(one+cost[i-1], two+cost[i-2])
            two = tmp
        last = len(cost)-1
        second_last = len(cost)-2
        return min(one+cost[last], two+cost[second_last])
        



