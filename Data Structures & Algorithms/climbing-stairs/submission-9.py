class Solution:
    stairs = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if n in self.stairs:
            return self.stairs[n]
        self.stairs[n] = self.climbStairs(n-2) + self.climbStairs(n-1)

        return self.stairs[n]
        
        