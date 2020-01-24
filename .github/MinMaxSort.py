stocks = {'GOOG' : 520.54, 'FB' : 76.54, 'YHOO' : 39.28 , 'AMZN' : 306.21, 'AAPL' : 99.76}

# - SPLITTING THIS INTO A LIST OF KEYS AND VALUES

# - You can't sort a dictionary, but you can sort a zipped list (of touples). List thrown in first is how its sorted.

print(min(zip(stocks.values(), stocks.keys()))) # - Lowest price

print(max(zip(stocks.values(), stocks.keys()))) # - Highest Price

print(sorted(zip(stocks.values(), stocks.keys()))) # - Entire list sorted by price.

print(sorted(zip(stocks.keys(), stocks.values()))) # - Entire list sorted by name.