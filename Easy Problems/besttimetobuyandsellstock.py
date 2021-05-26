
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
# day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

#Attempt #1 - time limit exceeded / not sure if it works for every case
# def maxProfit(prices):
#     """
#     :type prices: List[int]
#     :rtype: int
#     """
#     buyDay = 0
#     maxProfit = 0
#     counter = 0
#     length = len(prices)
#     profit = False

#     for price in range((len(prices) - 1), -1, -1):
#         if prices[price] < prices[price - 1]:
#             profit = True
#             break
#     if profit == False:
#         return 0

#     while(counter < length):
#         for price in range(len(prices)):
#             if prices[price] < prices[buyDay]:
#                 buyDay = prices.index(prices[price])

#         if buyDay == len(prices):
#             prices.remove(prices[buyDay])
#             break

#         for price in range(buyDay, len(prices)):
#             currentProfit = prices[price] - prices[buyDay]
#             if currentProfit > maxProfit:
#                 maxProfit = currentProfit
        
#         prices.remove(prices[buyDay])
#         buyDay = 0
#         counter += 1

#     return maxProfit

#Attempt #2 - ran in 804 ms and took 22.8 MB of storage
import sys

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    minPrice = sys.maxint
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        elif (price - minPrice) > maxProfit:
            maxProfit = price - minPrice
    return maxProfit

#Testing
prices1 = [7,1,5,3,6,4]
print(maxProfit(prices1))

prices2 = [7,6,4,3,1]
print(maxProfit(prices2))

prices3 = [2,4,1]
print(maxProfit(prices3))

prices4 = [1,1,0]
print(maxProfit(prices4))

prices5 = [4,7,1,2]
print(maxProfit(prices5))

prices6 = [7,11,1,2,4]
print(maxProfit(prices6))
