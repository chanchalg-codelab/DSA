class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        maximum = 0
        minimum = prices[0]

        for num in prices:
            if num < minimum:
                minimum = num

            profit = num - minimum
            
            if profit > maximum:
                maximum = profit

        return maximum
    