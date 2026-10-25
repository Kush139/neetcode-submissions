class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = usage = tc = 0

        for i in range(len(gas)):
            usage += gas[i]
            tc += cost[i]
            if tc > usage:
                start = i+1
                usage = 0 
                tc = 0
        return start if sum(gas) >= sum(cost) else -1

