class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:].zfill(32)
        total = 0
        for i in range(len(x)):
            total = total+int(x[i])*(2**i)
        return total