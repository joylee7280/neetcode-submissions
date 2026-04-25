class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = []
        while(n>0):
            re = n%2
            bit.append(re)
            n = n//2
        # print(bit)
        return(bit.count(1))

