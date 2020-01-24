import heapq

grades = [32, 43, 654, 34, 132, 66, 99, 532]

# I want the three highest grades.

print(heapq.nlargest(3, grades)) # 3 largest values from grades.

# This is useful for data sets like this...


stocks = [
{'ticker': 'AAPL', 'price': 2056781},
{'ticker': 'POOP', 'price': 2245601},
{'ticker': 'FART', 'price': 23501},
{'ticker': 'POO', 'price': 223401},
{'ticker': 'PEE', 'price': 291}]
# - I want the two cheapest stocks.

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price'])) # - Last 2 smallest price from stocks

