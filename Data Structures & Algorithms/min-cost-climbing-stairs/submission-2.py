class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #dp[len(cost)-1] = cost[-1]
        #dp[len(cost)-2] = cost[-2]
        #dp[i] = min(cost[i+1), cost[i+2]
        #dp[i] = min cost to get to top from there

        #dp[i] = min cost to reach step i
        dp = {}
        dp[0] = 0
        dp[1] = 0

        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        last = len(cost)-1
        second_last = len(cost)-2
        return min(dp[last]+cost[last], dp[second_last]+cost[second_last])
        



