class Solution:
    def climbStairs(self, n: int) -> int:
        array = [0]*(n+1)
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            for i in range(3,n+1,1):
                array[1] = 1
                array[2] = 2
                array[i] = array[i-1]+array[i-2]
            return array[n]
