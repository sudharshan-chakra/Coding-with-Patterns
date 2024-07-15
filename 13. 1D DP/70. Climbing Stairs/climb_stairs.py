class Solution:
    def climbStairs(self, n: int) -> int:
        climber = {0:0, 1:1, 2:2}

        def climb(k):
            if k in climber:
                return climber[k]

            climber[k] = climb(k-1) + climb(k-2)
            return climber[k]
        
        climb(n)
        return climber[n]