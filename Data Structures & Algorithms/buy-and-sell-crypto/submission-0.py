class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 100
        gap = 0
        for i in prices:
            if i < minimum:
                minimum = i
            if i-minimum > gap:
                gap = i-minimum
        return gap
