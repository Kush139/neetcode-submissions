class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        l = 0
        r = 0
        total_cost = 0
        usage = 0
        while l < len(gas):
            usage += gas[r]
            total_cost += cost[r]
            if total_cost > usage:
                if r > l:
                    l = r = r+1
                else:
                    l += 1
                    r = l
                total_cost = 0
                usage = 0
            else:
                r += 1
                if r > len(gas) - 1:
                    r = 0
                if r == l:
                    return l
        print(usage)
        print(total_cost)
        print(r)
        return -1


        

        #[1,2,3,4] usage
        #[2,3,4,1] cost

        #[1,2,3,4] usage
        #[2,2,4,1] cost

        #[4,1,2,3]
        #[1,2,2,4

        #[3,4,1,2]
        #[4,1,2,2]

        #[1,2,3,4]
        #[3,3,3,3]

        #[3,4,1,2]
        #[3,3,3,3]