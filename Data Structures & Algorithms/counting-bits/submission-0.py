class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range(n+1):
            array = []
            while num!=0:
                a = num%2
                num = num//2
                array.append(a)
            count = array.count(1)
            output.append(count)
        return output


